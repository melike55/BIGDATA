from bs4 import BeautifulSoup
import requests
import re
import time
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("C:\\Users\\Lenovo\\Desktop\\BIGDATA\\BuyukVeri\\buyukveriCredentials.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://buyukveri-5d9ba-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")

while True:
    mevcutID = db.reference("/id").get()
    mevcutID = mevcutID['id']


    def idArttırma(mevcutID):
        mevcutID = db.reference("/id").get()
        mevcutID = mevcutID['id']
        mevcutID = mevcutID + 1
        db.reference("/id").update({"id": mevcutID})
        print("ID 1 ARTTIRILDI . Yeni id : ", mevcutID)


    def idAzaltma(mevcutID):
        mevcutID = db.reference("/id").get()
        mevcutID = mevcutID['id']
        mevcutID = mevcutID - 1
        db.reference("/id").update({"id": mevcutID})
        print("ID 1 AZALTILDI . Yeni id : ", mevcutID)


    def idOgrenme():
        mevcutID = db.reference("/id").get()
        mevcutID = mevcutID['id']
        return print("Şu anki mevcut id : ", mevcutID)


    url = input("Lütfen URL Giriniz : ")


    def MakaleYukleme(mevcutID, url, tur, makale):
        mevcut_urller = db.reference("/Makaleler").get().keys()
        idArttırma(mevcutID)
        hatasizMi=1
        data = {
            "id": mevcutID,
            "url": url,
            "tur": tur,
            "makale": makale
        }
        mevcut_urller = list(mevcut_urller)
        #print(mevcut_urller)
        for i in range(0, len(mevcut_urller)):
            yer = "/Makaleler/" + str(mevcut_urller[i]) + "/url"
            eskiurller = db.reference(yer).get()
            if url == eskiurller:
                print("\n",2, "",40 , "Bu Makale Daha Once Yuklenmis", ""*40,"\n"*2, sep="\n")
                print("Hatalı eklemeden dolayı id azaltılıyor ! ")
                idAzaltma(mevcutID)
                hatasizMi=0
        if hatasizMi:
            db.reference("/Makaleler").push(data)


    def Webrazzi(url):
        print("Bu bir Webrazzi linki . Tur TEKNOLOJİ olarak seçildi ")
        page = requests.get(url)
        print(url)
        tur = "Teknoloji"
        soup = BeautifulSoup(page.text, 'html')
        makale = soup.find('div', class_='single-post-content').text.strip()
        makale = makale.replace(u'\xa0', '')
        makale = makale.replace(u'\n', '')
        MakaleYukleme(mevcutID, url, tur, makale)


    def Medium(url):
        print("Bu bir Medium Linki . Tür girmeniz gerekiyor ")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        soup = soup.find_all('p')
        tur = input("Makale türünü girin (haber, spor, vs.): ")
        clean_titles = []
        bad_words = ["Sign up", "Sign in", "Member-only story", "Follow", "Share", "Listen"]
        for tag in soup:
            clean_title = tag.text.strip()  # Remove leading and trailing whitespace
            if clean_title in bad_words:
                pass
            else:
                clean_titles.append(clean_title)
        makale = "".join(clean_titles)
        MakaleYukleme(mevcutID, url, tur, makale)


    def Teknoblog(url):
        print("Bu bir Teknoblog linki . Tur TEKNOLOJİ olarak seçildi ")
        page = requests.get(url)
        tur = "Teknoloji"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        soup = soup.find_all('p')
        clean_titles = []
        for tag in soup:
            clean_title = tag.text.strip()
            clean_titles.append(clean_title)
        makale = ''.join(clean_titles)
        makale = makale.replace(u'\xa0', '')
        makale = makale.replace(u'\n', '')
        MakaleYukleme(mevcutID, url, tur, makale)


    def DoktorSitesi(url):
        print("Bu bir Doktor Sitesi Linki , O yuzden tur SAGLIK/PSİKOLOJİ olarak seçildi")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        soup = soup.find_all('p')
        tur = "Saglik/Psikoloji"
        clean_titles = []
        makalesonu = "kez okundu"
        for tag in soup:
            clean_title = tag.text.strip()  # Remove leading and trailing whitespace
            if makalesonu in clean_title:
                break
            clean_titles.append(clean_title)
        makale = ''.join(clean_titles)
        makale = makale.replace(u'\xa0', '')
        makale = makale.replace(u'\n', '')
        MakaleYukleme(mevcutID, url, tur, makale)


    def AdaletBlog(url):
        print("Bu bir Adalet Blog Linki , O yuzden tur HUKUK olarak seçildi")
        tur = "Hukuk"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        soup = soup.find_all('p')
        clean_titles = []
        makalesonu = "E-posta adresiniz yayınlanmayacak. Gerekli alanlar * ile işaretlenmişlerdir"
        for tag in soup:
            clean_title = tag.text.strip()
            if clean_title == makalesonu:
                break
            clean_titles.append(clean_title)

        makale = ''.join(clean_titles)
        makale = makale.replace(u'\xa0', '')
        makale = makale.replace(u'\n', '')
        MakaleYukleme(mevcutID, url, tur, makale)



    def Futuristika(url):
        print("Bu bir Futuristika Linki , O yuzden tur Sanat olarak seçildi")
        tur = "Sanat"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')
        soup = soup.find_all('p')
        clean_titles = []
        for tag in soup:
            clean_title = tag.text.strip()
            clean_titles.append(clean_title)
        makale = ''.join(clean_titles)
        makale = makale.replace(u'\xa0', '')
        makale = makale.replace(u'\n', '')
        MakaleYukleme(mevcutID, url, tur, makale)

    def SporEgitimi(url):
        print("Bu bir SporEgitimi linki . Tur Spor olarak seçildi ")
        tur = "Spor"
        page = requests.get(url)
        print("********************"+ url)
        soup = BeautifulSoup(page.text, 'html')
        soup = soup.find_all('p')
        clean_titles = []
        for tag in soup:
            clean_title = tag.text.strip()
            clean_titles.append(clean_title)
        makale = ''.join(clean_titles)
        makale = makale.replace(u'\xa0', '')
        makale = makale.replace(u'\n', '')
        MakaleYukleme(mevcutID, url, tur, makale)




    parcaUrl = url.split(".")
    print(parcaUrl)
    if parcaUrl[0] == "https://webrazzi":
        Webrazzi(url)
    if parcaUrl[0] == "https://medium.com/t%C3%BCrkiye":
        Medium(url)
    if parcaUrl[1] == "teknoblog":
        Teknoblog(url)
    if parcaUrl[1] == "doktorsitesi":
        DoktorSitesi(url)
    if parcaUrl[0] == "https://adalet":
        AdaletBlog(url)
    if parcaUrl[0] == "https://futuristika":
        Futuristika(url)
    if parcaUrl[1] == "https://www.sporegitimi.com/tr/blog/":
        SporEgitimi(url)