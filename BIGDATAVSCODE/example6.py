import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import json

# Web sayfasından verileri çekme
url = "https://medium.com/t%C3%BCrkiye/%C3%B6fke-sorunlar%C4%B1n%C4%B1-y%C3%B6netmenin-10-sa%C4%9Fl%C4%B1kl%C4%B1-yolu-ve-4-pratik-faydas%C4%B1-598a5d647a30"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Blog başlığını ve içeriğini alma
title = soup.find("h1").text.strip()
content_paragraphs = soup.find_all("p")

content = ""
for paragraph in content_paragraphs:
    content += paragraph.text.strip() + "\n"

# Kafka'ya göndermek için veriyi hazırlama
message = {"title": title, "content": content}

# Kafka producer oluşturma
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Kafka'ya veri gönderme
producer.send('blog-verisi', json.dumps(message).encode('utf-8'))

print("Blog verisi Kafka'ya gönderildi.")
