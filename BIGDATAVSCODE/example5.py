import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kafka import KafkaConsumer
import json

# Firebase'e bağlanmak için kimlik doğrulaması
cred = credentials.Certificate("C:\\Users\\Lenovo\\Desktop\\bigdata-eda45-firebase-adminsdk-vi4mt-ffd30c28d4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bigdata-eda45-default-rtdb.firebaseio.com/'
})

# Firebase Realtime Database referansı
ref = db.reference('/bloglar')

# Kafka tüketiciyi başlat
consumer = KafkaConsumer('blog-verisi', bootstrap_servers='localhost:9092', group_id='my-group')

for message in consumer:
    # Kafka'dan gelen JSON verisini yükle
    veri = json.loads(message.value.decode('utf-8'))
    
    # Veriyi Firebase'e kaydet
    ref.push(veri)
    
    print("Blog verisi Firebase'e kaydedildi.")
