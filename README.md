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
