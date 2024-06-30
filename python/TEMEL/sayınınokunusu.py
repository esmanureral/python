#Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.


birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birincirakam=sayi%10 #Bu, sayıyı 10'a böler ve kalanını alır.
    ikincirakam=sayi//10 #Bu, sayıyı 10'a böler ve tam sayı kısmını alır.
    
    return onlar[ikincirakam]+" "+birler[birincirakam]

sayi=int(input("sayi:"))
print(okunus(sayi))