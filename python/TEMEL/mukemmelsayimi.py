#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def mukemmelsayimi(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi%i==0):
            toplam+=i
    return toplam==sayi


for i in range(1,1000):
    if(mukemmelsayimi(i)):
        print("mukemmel sayi:",i)
            
            