"""
Hayvan Sinifi -> Bütün hayvanlarin ortak özelliklerinin toplandiği sinif olacak.
Köpek Sinifi -> Bu sinif, hayvan sinifindan miras alan bir sinif olacak. Ayrica bu sinifa köpeklere ait ek özellikler ve metodlar ekleyin.
Kuş sinifi -> Bu sinif, hayvan sinifindan miras alan bir sinif olacak. Ayrica bu sinifa kuşlara ait ek özellikler ve metodlar ekleyin.
At sinifi -> Bu sinif, hayvan sinifindan miras alan bir sinif olacak. Ayrica bu sinifa atlara ait ek özellikler ve metodlar ekleyin.
"""
class Hayvan():
    def __init__(self, türü, göz_şekli, göz_rengi, ayak_sayisi, hareket_hizi):

        print("Hayvan sinifinin init fonksiyonu...")

        self.türü = türü
        self.göz_şekli = göz_şekli
        self.göz_rengi = göz_rengi
        self.ayak_sayisi = ayak_sayisi
        self.hareket_hizi = hareket_hizi

    def bilgilerigöster(self):

        print("Hayvan sinifinin bilgileri...")

        print("""
        Tür: {}
        Göz şekli: {}
        Göz rengi: {}
        Ayak ayak_sayisi: {}
        hareket_hizi: {}
        """.format(self.türü,self.göz_şekli,self.göz_rengi, self.ayak_sayisi, self.hareket_hizi))
        
    def hareketet(self, hareket_şekli):
        print("{} hareket ediyor".format(hareket_şekli))    
        
        
    def hizlandir(self, hizlanma_miktari):
        print("hizlandiriliyor...")
        self.hareket_hizi = self.hareket_hizi + hizlanma_miktari    
        print("Yeni hiz: {}".format(self.hareket_hizi))    
        
Hayvan1 = Hayvan("köpek", "yuvarlak", "kahverengi", 2, 10 )
print(Hayvan1)
Hayvan1.bilgilerigöster()
Hayvan1.hareketet("yürüyerek")