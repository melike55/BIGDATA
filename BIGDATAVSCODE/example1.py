import requests
from bs4 import BeautifulSoup


def blog_yazilari_cek(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    # Web sitesinden sayfa içeriğini indirme
    response = requests.get(url,headers=headers)
    # İndirilen içeriği BeautifulSoup kütüphanesiyle ayrıştırma
    soup = BeautifulSoup(response.text, 'html.parser')
    # Blog yazılarının bulunduğu etiketleri belirleme (örneğin, <div class="blog-post"> gibi)
    blog_posts = soup.find_all('div', class_='px-6 py-10 md:py-12 md:px-10 xl:p-2 0')
    
    blog_yazilari = []
    # Her bir blog yazısının içeriğini ve başlığını alıp bir liste olarak saklama
    for post in blog_posts:
        baslik = post.find('href').text.strip()  # Örnek olarak <h2> etiketinden başlığı çekiyoruz
        icerik = post.find('div', class_='px-6 py-10 md:py-12 md:px-10 xl:p-20').text.strip()  # Örnek olarak içerik <div class="content"> etiketinden çekiliyor
        blog_yazilari.append({'heading-subtle': baslik, 'content-repository-content prose max-w-md-lg mx-auto flow-root getShouldDisplayAdsAttribute has-image-links': icerik})
    
    return blog_yazilari

# Blog yazılarının bulunduğu web sitesinin URL'sini belirleyin
url = 'https://www.health.harvard.edu/blog'

# Fonksiyonu kullanarak blog yazılarını çekme
yazilar = blog_yazilari_cek(url)

# Elde edilen blog yazılarını ekrana yazdırma
for yazı in yazilar:
    print("Başlık:", yazı['baslik'])
    print("İçerik:", yazı['icerik'])
    print("\n")
