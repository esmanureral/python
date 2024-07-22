"""
 Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri 
 *isimlere* göre sıralı bir şekilde yazdırmaya çalışın.
 
 """
 
 
isim = ["Cengizhan","Kerim","Tarık","Ezgi","Kemal","İlkay","Esmanur"]
soyisim = ["Kaya","Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya"]
 
liste=list(zip(isim,soyisim)) #zip iki ifadeyi birleştirir.
list.sort  #artan sıraya göre sıralar.

for i,j in liste:
    print(i,j)
