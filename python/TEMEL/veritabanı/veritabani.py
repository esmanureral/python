#Relational Database(ilişkisel veritabanları):Tablolardan oluşur.Mysql,Sqlite vs.
#DocumentBased Database(Döküman Veritabanları):Dökümanlardan oluşur.MongoDb,Azure D.


#TABLO OLUŞTURDUK VE VERİTABANINA BAĞLANDIK..
import sqlite3
con=sqlite3.connect("kütüphane.db") #kütüphane.db veritabanını oluşturup bağlanıyoruz
cursor=con.cursor()#Database üzerinde Sql sorgularını çalıştırmak için imleç oluşturduk.



def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT, Yazar TEXT,Yayınevi TEXT,Sayfa_sayisi INT)")
    con.commit()
tablo_oluştur()
con.close() #bağlantıyı kestik.


#KİTAPLIK TABLOSU OLUŞTURMA

#1)
#CREATE TABLE kitaplık (isim TEXT, Yazar TEXT,Yayınevi TEXT,Sayfa_sayisi INT)
#Bu sorguyu ard arda çalıştırırsak hata alırız.


#2)
#CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT, Yazar TEXT,Yayınevi TEXT,Sayfa_sayisi INT)
#tablo yoksa oluşturacak.

