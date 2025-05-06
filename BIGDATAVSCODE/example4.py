import requests
from bs4 import BeautifulSoup

URL='https://medium.com/t%C3%BCrkiye/%C3%B6fke-sorunlar%C4%B1n%C4%B1-y%C3%B6netmenin-10-sa%C4%9Fl%C4%B1kl%C4%B1-yolu-ve-4-pratik-faydas%C4%B1-598a5d647a30'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
sayfa=requests.get(URL,headers=headers)
icerik=BeautifulSoup(sayfa.content,'html.parser')
#print(icerik)

blogBasligi=icerik.find("h1").get_text()
print(blogBasligi)

blogIcerigi=icerik.find_all("p")
print(blogIcerigi)