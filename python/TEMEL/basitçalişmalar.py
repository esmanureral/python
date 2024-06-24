print(3+4);
a=5;
b=3;
c=a+b;
print(c);

#Değişkenleri değiştirme kolay yöntem

a=2;
b=1;
a,b=b,a
print(b);

#Bölmede tam sayı bölmesi için // kullanılabilir

a=345;
b=36;
c=a/b;
print(c);
c=a//b;
print(c);

#üs ifadesini kullanarak karekök bulma

a=36;
a=a**0.5;
print(a);

#küp kök alma
a=8;
a=a**(1/3);
print(a);

#Parçalama işlemleri [başlangıç:bitiş:artırma]
yazi="Python Programlama Dili"
a=yazi[4:10];#4.indexten başla 10 a kadar 10 dahil değil 'on pro'
print(a);
a=yazi[:10]; #baştan 10.indexe kadar git 'python pro'
print(a); 
a=yazi[:-1]; #baştan başla son indexi alma 'Python Programlama Dil'
print(a);
a=yazi[::2]; #baştan sona kadar 2 2 atla 'Pto rgalm ii'
print(a);

#Dizi Uzunluğu
string="Merhaba";
print(len(string)); #7 çıktısını verir

#String Birleştirme

a="Esmanur "
a= a +  "Eral"
print(a)

#not:herhangi bir stringin belli bir indexindeki değeri direkt atama yöntemiyle değiştiremiyoruz.
#a = "Python"
#a[0] = 'C'
#a

# float: tam sayıyı ondalığa çevirir.
# int: ondalıklı sayıyı tam sayıya çevirir.
# str: tam sayıyı stringe çevirir.
# \n: aşağı satırdan devam.


# sep parametresi: print() fonksiyonunda kullanılır değerlerin arasına istediğimiz karakterin yazdırılmasını sağlar

print("esmanur ","eral",sep=" :D ") #çıktısı:esmanur  :D eral

#yıldız parametresi:print() fonksiyonunda kullanılır değerlerin arasına boşluk koyar

print(*"esmanur") # e s m a n u r 

#liste.append() ekleme
#liste.sort()   küçükten büyüğe sıralama

#input("bir sayı gir")

#aşağıdaki örnekte sayıların string oldugunu unutma toplama yanyana yazar. a=4,b=3,c=2 ise sonuc 432 dir.
a = input("Birinci Sayı:")
b = input("İkinci Sayı:")
c = input("Üçüncü Sayı:")
 
print("Toplamları:",a+b+c)




#in : listede olup olmadığını kontrol eder.

liste=[1,2,3,4,5]
for eleman in liste:
    print(eleman) #çıktısı: 1 2 3 4 5 alt alta
    
#LİSTEDEKİ SAYILARI FOR DÖNGÜSÜYLE TOPLAMA:  
toplam=0
liste=[1,2,3,4,5]
for eleman in liste:
    toplam=toplam+eleman
print("Toplam:",toplam) 

#LİSTEDEKİ ÇİFT SAYILARI FOR DÖNGÜSÜYLE YAZDIRMA:
liste=[1,2,3,4,5]
for eleman in liste:
    if eleman%2==0:
        print("çift sayılar:",eleman)
        
#KARAKTER DİZİLERİ ÜZERİNDE GEZİNME:

s="PYTHON"
for karakter in s:
    print(karakter)  #PYTHON daki harfleri tek tek yazdırır.
    

#LİSTEDEKİ TEK SAYILARI TOPLAMA

liste = [2,1,10,2,23,1,56,3]
toplam=0
for i in liste:
    if(not (i%2==0)):
        toplam=toplam+i
print(toplam)

#RANGE() FONSKİYONU

print(*range(0,20)) #0dan 20 ye kadar olan sayıları yazdırır.20 dahil değil.
print(*range (1,100,2)) #1den 100e kadar olan sayıların 2 şer atlayarak yazdırır.
print(*range(20,1))#bu şekil azaltarak gitmez.
print(*range(20,1,-1))#bu şekilde 20,19,18..2 gider.


#ARTAN YILDIZLAR

"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
"""

for i in range(1,10):
    print("* "*i)


#LİST COMPREHENSİON:liste üretmek ve oluşturmak.

#bir listeyi başka bir listeye aktarma

liste1=[1,2,3,4,5]
liste2=[i for i in liste1]
print(liste2)


liste3=[3,4,5,6,8,9]
liste4=[i*2 for i in liste3]
print(liste4)

liste5=[(1,2),(3,4)]
liste6=[i*j for i,j in liste5]
print(liste6)
