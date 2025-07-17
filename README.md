## Legal Disclaimer / Yasal Uyarı
English:
This tool is intended for educational and ethical testing purposes only. It must not be used to access any accounts, systems, or data without explicit permission from the owner. The developer is not responsible for any misuse or damage caused by the use of this tool. By using this software, you agree to comply with all applicable laws and regulations.

Türkçe:
Bu araç yalnızca eğitim ve etik test amaçları için tasarlanmıştır. Sahiplerinden açık izin almadan herhangi bir hesaba, sisteme veya veriye erişmek için kullanılmamalıdır. Bu aracın yanlış kullanımından veya sebep olduğu zararlardan geliştirici sorumlu değildir. Bu yazılımı kullanarak, yürürlükteki tüm yasalara ve yönetmeliklere uyacağınızı kabul etmiş olursunuz


## Outlook Account Verification Bot 🚀
## 🇬🇧 Guide in English 🇬🇧

This project is a Python-based bot that automatically verifies Outlook (Microsoft) accounts using proxy support and a headless Chrome browser.
With multithreading and dynamic proxy usage, it can check accounts at high speed.

## Features
Automatically fetches proxy lists from proxy APIs and tests them for availability

Uses headless Chrome with undetected_chromedriver for realistic browser behavior

Detects banned proxies and replaces them with fresh ones

Runs multiple threads to check many accounts in parallel

Saves successful logins to the valid_accounts.txt file

Logs statistics such as number of successes, failures, and errors

## Requirements
Python 3.8+

undetected-chromedriver

Selenium

Requests

Install dependencies with:

`pip install undetected-chromedriver selenium requests`


## Usage
Write the accounts you want to check in accounts.txt in the format:

`email:password`
Proxy lists will be automatically fetched from APIs as needed.

To run the script:

`python -m checker.py`
After the check, all valid accounts will be saved to valid_accounts.txt.

## Files
accounts.txt: List of accounts to be checked

valid_accounts.txt: Stores successfully verified accounts

your_script_name.py: Main Python script

## How It Works
Pulls and validates proxies from public proxy APIs. (You can add yours, if  you want)

Launches a separate thread for each account and attempts login using headless Chrome

Detects bans and replaces blocked proxies with working ones

Saves successful logins to a file

## Important Notes
Script uses undetected_chromedriver to bypass Microsoft's bot protection

The number of proxies used is adjusted based on the number of accounts

Make sure your proxy API sources are active for best performance

Using your own proxy APIs will reduce the number of errors



## 🇹🇷 Türkçe Rehber 🇹🇷



# Outlook Hesap Doğrulama Botu 🚀

Bu proje, **Python** kullanarak Outlook (Microsoft) hesaplarını proxy destekli ve headless Chrome ile otomatik olarak doğrulayan bir bot içerir.  
Çoklu iş parçacığı (multithreading) ve dinamik proxy kullanımı ile yüksek hızda hesap kontrolü sağlar.

---

## Özellikler

- Proxy API’lerinden otomatik olarak proxy listesi çekme ve çalışma durumunu test etme  
- Headless (görünmez) Chrome kullanarak gerçekçi tarayıcı kontrolü (undetected_chromedriver)  
- Proxy banlarını algılama ve banlı proxyleri listeden çıkarıp yenisini alma  
- Çoklu thread ile aynı anda çok sayıda hesabı hızlı kontrol edebilme  
- Başarılı hesapları `valid_accounts.txt` dosyasına kaydetme  
- Loglama ve istatistik takibi (başarılı, başarısız, hata sayıları)

---

## Gereksinimler

- Python 3.8+  
- [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver/)  
- Selenium  
- Requests  

Kurulum için:

pip install undetected-chromedriver selenium requests
## Kullanım
accounts.txt dosyasına email:password formatında kontrol etmek istediğiniz hesapları yazın.

Proxy ihtiyacına göre proxy listeleri otomatik çekilecektir.

Aşağıdaki komut ile scripti çalıştırın:

python -m checker.py
İşlem sonunda başarılı hesaplar valid_accounts.txt dosyasına kaydedilir.

## Dosyalar
accounts.txt: Kontrol edilecek hesapların listesi

valid_accounts.txt: Başarılı hesapların kaydedildiği dosya

your_script_name.py: Ana Python scripti

## Nasıl Çalışır?
Proxy API’lerinden proxyleri çeker ve test eder.

Her hesap için yeni bir thread açar ve headless Chrome ile login denemesi yapar.

Ban tespiti yaparak proxyyi çıkarır ve yenisini çeker.

Başarılı hesapları dosyaya kaydeder.

## Önemli Notlar
Script, Microsoft’un güvenlik önlemlerine takılmamak için undetected_chromedriver kullanır.

Proxy sayısı, hesap sayısına göre otomatik ayarlanır.

Proxylerin sağlıklı çalışması için API bağlantılarının aktif olması gerekir.

Kendi API-lerinizi kullanmaniz daha az **ERROR**'a sebep olur.
