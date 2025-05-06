import requests
from bs4 import BeautifulSoup

def scrape_blog_titles_and_topics(url, num_posts=5):
    # Web sitesinden veri çekme
    response = requests.get(url)
    if response.status_code != 200:
        print("Hata: Sayfa yüklenemedi.")
        return
    
    # BeautifulSoup kullanarak HTML içeriğini ayrıştırma
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Blog yazılarını bulma
    blog_posts = soup.find_all('h2', class_='blog-listing__title')[:num_posts]
    
    # Başlık ve konuları saklamak için boş bir liste oluşturma
    posts_data = []

    # Her bir blog yazısı için başlık ve konuyu alıp listeye ekleme
    for post in blog_posts:
        # Başlık
        title = post.text.strip()
        
        # Konu
        # Her blog yazısının sayfasına gidip konuyu alacağız
        post_url = post.find('a')['href']
        post_response = requests.get(post_url)
        post_soup = BeautifulSoup(post_response.content, 'html.parser')
        topic_tag = post_soup.find('meta', property='article:tag')
        topic = topic_tag['content'] if topic_tag else 'Konu bulunamadı'
        
        # Başlık ve konuyu bir sözlük olarak listeye ekleme
        posts_data.append({'title': title, 'topic': topic})
    
    return posts_data

# Web sitesinin URL'si
url = 'https://www.health.harvard.edu/blog'

# Fonksiyonu kullanarak blog yazılarından başlık ve konuları çekme
blog_data = scrape_blog_titles_and_topics(url, num_posts=5)

# Başlık ve konuları yazdırma
for i, post in enumerate(blog_data, 1):
    print(f"Blog Yazısı {i}:")
    print("Başlık:", post['title'])
    print("Konu:", post['topic'])
    print()
