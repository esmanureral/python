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

