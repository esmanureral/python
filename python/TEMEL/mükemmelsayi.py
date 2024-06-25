#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
# Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

sayi=int(input("sayi giriniz:"))

i=1
toplam=0

while(i<sayi):
    if(sayi%i==0):
        toplam=toplam+i
    i+=1

if(toplam==sayi):
    print("girilen sayi mükemmel sayıdır.")
else:
    print("mükemmel sayi değildir")
    

