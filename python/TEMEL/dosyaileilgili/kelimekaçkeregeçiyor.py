class Dosya():
    def __init__(self):
        with open("metin.txt", "r", encoding="utf-8") as file:  # dosya okuma
            dosyaiçeriği = file.read()
            kelimeler = dosyaiçeriği.split()  # noktalardan sonra boşluk koyup ayırdı.
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)

            #for i in self.sade_kelimeler:
                #print(i) (tek tek kelimeleri yazdırdı.)
                
    def tum_kelimeler(self):  
        kelimeler_kumesi=set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
            
        print("Tüm Kelimeler...")
        
        for i in kelimeler_kumesi:
            print(i)
            print("*****************************")
        
    def kelime_frekansı(self):
        kelime_sözlük=dict()
        
        for i in self.sade_kelimeler:
            if(i in kelime_sözlük):
                kelime_sözlük[i]+=1
            else:
                kelime_sözlük[i]=1
        
        for kelime,sayi in kelime_sözlük.items():
            print("{} kelinmesi {} defa geçiyor..".format(kelime,sayi))
            
            

dosya = Dosya()  # bunu yazmadan dosya içeriği okumuyor.
dosya.tum_kelimeler() #her bir kelimeden bir kere olacak şekilde yazdırdı
dosya.kelime_frekansı() #kelimeler kaç kere geçiyor. 