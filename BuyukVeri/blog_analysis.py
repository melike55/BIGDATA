from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col, lower
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.ml import Pipeline
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('C:\\Users\\Lenovo\\Desktop\\BIGDATA\\BuyukVeri\\buyukveriCredentials.json')
firebase_admin.initialize_app(cred, {"databaseURL" : "https://buyukveri-5d9ba-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")

def verileri_firebase_cek(collection_name):
    dokumanlar = veritabani.collection(collection_name).stream()
    veriler = [(dok.to_dict()['makale'], dok.to_dict()['tur']) for dok in dokumanlar]
    return veriler



turkce_baglaclar = set(["ve", "veya", "ile", "çünkü", "ama", "fakat", "ancak", "dolayısıyla", "çünkü", "ancak", "gibi"])


spark = SparkSession.builder \
    .appName("TF-IDF Metin Sınıflandırma") \
    .getOrCreate()


veriler = verileri_firebase_cek("Makaleler")
df = spark.createDataFrame(veriler, ["id", "metin", "etiketler"])


df = df.withColumn("metin_kucuk", lower(col("metin")))


kelime_tokenizer = Tokenizer(inputCol="metin_kucuk", outputCol="kelimeler")
baglac_silici = StopWordsRemover(inputCol="kelimeler", outputCol="suzulmus_kelimeler").setStopWords(list(turkce_baglaclar))


hashingTF = HashingTF(inputCol="suzulmus_kelimeler", outputCol="ham_ozellikler", numFeatures=100)
idf = IDF(inputCol="ham_ozellikler", outputCol="ozellikler")


etiket_indexer = StringIndexer(inputCol="etiketler", outputCol="etiket")


pipeline = Pipeline(stages=[kelime_tokenizer, baglac_silici, hashingTF, idf, etiket_indexer])


model = pipeline.fit(df)
sonuc = model.transform(df)


sonuc.select("id", "ozellikler", "etiket").write.mode("overwrite").parquet("blog_ozellikler.parquet")


df_sonuc = spark.read.parquet("blog_ozellikler.parquet")
df_sonuc.show(truncate=False)