import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response=requests.get("https://www.health.harvard.edu/blog", headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
print(soup.title.string)
for link in soup.find_all("a"):
    print(link.get("href"))
    

headers2 = {
   'User-Agent':'(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response2=requests.get("https://www.technewsworld.com/section/tech-blog", headers=headers2)
soup2=BeautifulSoup(response2.text,"html.parser")
print(soup2.title.string)
for link in soup2.find_all("a"):
    print(link.get("href"))
    

headers3 = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response3=requests.get("https://www.artworkarchive.com/blog", headers=headers3)
soup3=BeautifulSoup(response3.text,"html.parser")
print(soup3.title.string)
for link in soup3.find_all("a"):
    print(link.get("href"))
    