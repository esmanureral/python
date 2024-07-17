"""
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

isimler -----> ["Kerim","Tarik","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler -----> ["Yilmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sirasiyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdirin.

*Not: zip() fonksiyonunu kullanmaya çalişin. *
"""

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)
