#overriding(iptal etme):miras aldığımız metodla aynı isimle kendi sınıfımızda tekrar tanımlarsak,artık metodu çağırdımız metodumuz çalışacak

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("çalışan sınıfının init fonksiyonu")
        
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
    def bilgilerigöster(self):
        print("çalışan sınıfının bilgileri..")
        print("isim: {} \n  Maaş: {} \n departman: {} \n".format(self.isim,self.maaş,self.departman))
        
    def departman_değiştir(self,yeni_departman):
        self.departman=yeni_departman
            
class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişisayisi):
        print("yötenici sınıfının init fonksiyonu")
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
        self.kişisayisi=kişisayisi
        
    def zam_yap(self,zam_miktarı):
        self.maaş+=zam_miktarı
        
yönetici=Yönetici("esma",3000,"bilişim",10)
        
