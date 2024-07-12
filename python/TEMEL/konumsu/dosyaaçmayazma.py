"""
Dosya Açma: Open()
open(dosyaadi,dosyaerişmekipi)

W(write) DOSYA KİPİ
*Oluşturmak istediğimiz dosya yoksa dosyayi oluşturuyor
*Oluşturmak istediğimiz dosya varsa dosyayi silip tekrar oluşturuyor
"""
#wkipi diye text dosyam yoktu oluşturdu
open("wkipi.txt","w")
file=open("wkipi.txt","w")
file.close()

#aşağıdaki satır masaüstüne deneme adlı text dosyası oluşturdu.
file=open("C:/Users/esman/OneDrive/Masaüstü/deneme.txt","w")

#türkçe karakter olmadığı için yazdırdı. deneme text dosyasını ilk silip tekrar oluşturdu
#masaüstündeki değil oluşturdugumuz klasörde

file=open("deneme.txt","w")
print(file.write("Esmanur Eral\n"))
file.close()


file=open("deneme1.txt","w",encoding="utf-8")
print(file.write("Eşşmanur Eral"))
file.close()



""" A(append) kipi
 dosya yoksa oluşturulur.
 dosya varsa tekrar oluşturulmaz ekleme yapilir
"""

file=open("deneme.txt","a")
print(file.write("esmanur eral"))
file.close()


"""

DOSYA OKUMA
#r kipi
dosya varsa hata vermez
dosya yoksa FileNotFoundError verir

"""

file=open("deneme.txt","r")   #hata vermez



try:
  file=open("olmayandosya.txt","r") #hata verir
except FileNotFoundError:
    print("dosya bulunamadı")



#FOR DÖNGÜSÜYLE DOSYA OKUMA

file=open("okuma.txt","r",encoding="utf-8")

for i in file:
    print(i) #bu şekilde arada boşluklar vererek yazdırıyor
file.close()

file=open("okuma.txt","r",encoding="utf-8")

for i in file:
    print(i,end="") #boşluksuz yazdırır.
file.close()


#READ() İLE OKUMA
#hiç bir değer vermezsek bütün dosyayı okur.

file=open("okuma.txt","r",encoding="utf-8")

içerik=file.read()
print("dosyanın içeriği:")
print(içerik)


file=open("okuma.txt","r",encoding="utf-8")

içerik=file.read()
print("dosyanın içeriği:")
print(içerik)

içerik2=file.read()
print("dosyanın içeriği 2")
print(içerik2) #içerik tekrar yazdırmaz.


#READLİNE() İLE OKUMA
#her çağrıldığında dosyanın sadece bir satırını okur.Her seferinde imlec bir satır atlar.

file=open("okuma.txt","r",encoding="utf-8")
print(file.readline())
print(file.readline())



#DOSYAYI OTOMATİK KAPATMA
# with open(dosyaadi,dosyakipi) as file:

#DOSYAYI İLERİ GERİ SARMAK
#seek()
# imlec hangi byteda=tell()


with open("okuma.txt","r",encoding="utf-8") as file:
    print(file.tell())
    file.seek(15)
    print(file.tell())



#ilk imlec 3.byte geliyor 3.byten itibaren 8 tane karakter okunuyo
with open("okuma.txt","r",encoding="utf-8") as file:
    file.seek(3)
    içerik=file.read(8)
    print(içerik)



#r+ kipi
#hem okuma hem yazma

with open("degisikliyapma.txt","r+",encoding="utf-8") as file:
    print(file.read())


#txt dosyasında istediğimiz bytedan itibaren bir şeyler yazdırma
with open("degisikliyapma.txt","r+",encoding="utf-8") as file:
    file.seek(5)
    file.write("yazdırılan metin")
    print(file.read())




#DOSYANIN SONUNDA DEĞİŞİKLİK YAPMAK

with open("sona.txt","a",encoding="utf-8") as file:
    file.write("cengiz\n")
with open("sona.txt","r+",encoding="utf-8") as file:
    print(file.read())




#DOSYANIN BAŞINDA DEĞİŞİKLİK YAPMA
with open("başa.txt","r+",encoding="utf-8") as file:
    print(file.read())


#Dosya başına Rukiye eklendi.
with open("başa.txt","r+",encoding="utf-8") as file:
    içerik=file.read()
    içerik="Rukiye\n"+içerik
    print(içerik)


#DOSYA ORTASINA DEĞİŞİKLİK YAPMAK
with open("orta.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    print(liste)

with open("orta.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"Yahya Kemal\n")
    file.seek(0)
    for i in liste:
        file.write(i)
with open("orta.txt","r+",encoding="utf-8") as file:
    print(file.read())
