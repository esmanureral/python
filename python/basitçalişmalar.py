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

a="Esmanur ";
a= a +  "Eral";
print(a);

#not:herhangi bir stringin belli bir indexindeki değeri direkt atama yöntemiyle değiştiremiyoruz.
#a = "Python"
#a[0] = 'C'
#a
 