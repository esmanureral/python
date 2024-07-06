#özel metodlar

#   1) İNİT:init metodunu kendimiz tanımlarsak artık kendi init fonksiyonumuz çalışacaktır.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("Kitap Objesi oluşturuluyor..")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayısı=sayfa_sayısı
        self.tür=tür
        
Kitap1=Kitap("İstanbl Hatırası","Ahmet Ümit",561,"Polisiye")

#   2) STR: İçerik daha anlaşılır olur. 
#str metodunu kullanamdan print(kitap1) yazsak hata alırız.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("Kitap Objesi oluşturuluyor..")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayısı=sayfa_sayısı
        self.tür=tür
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
Kitap1=Kitap("İstanbl Hatırası","Ahmet Ümit",561,"Polisiye")
print(Kitap1)

#   3) LEN: Özel olarak tanımlarsak var olur.
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
     return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı

kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(len(kitap1))

#   4) DEL: Özel olarak tanımlarsak var olur.
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.......")
        
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
del kitap1