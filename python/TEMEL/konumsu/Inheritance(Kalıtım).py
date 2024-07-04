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
            
class Yönetici(Çalışan): #çalışandaki özellikler yöneticide oldu
    pass

yönetici=Yönetici("Mustafa",3000,"bilişim")
print(yönetici.bilgilerigöster())
yönetici.departman_değiştir("insan kaynakları")
print(yönetici.bilgilerigöster())

class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        self.maaş+=zam_miktarı
        
yönetici=Yönetici(  "esmanur",3500,"pazarlama")
print(yönetici.bilgilerigöster())
yönetici.zam_yap(5000)
print(yönetici.bilgilerigöster())
