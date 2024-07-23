"""
INSERT iNTO kitaplık VALUES ("İstanbul Hatırası","Ahmet Ümit",561)

"""

import sqlite3
con=sqlite3.connect("kütüphane.db") 
cursor=con.cursor()



def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT, Yazar TEXT,Yayınevi TEXT,Sayfa_sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute ("INSERT iNTO kitaplık VALUES ('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

veri_ekle()
    
con.close() 