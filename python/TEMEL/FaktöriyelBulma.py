print(""" SAYININ FAKTÖRİYELİNİ BULMA 
      ÇIKMAK İÇİN Q YA BASINIZ""")

while True:
    sayi=input("sayi gir.")
    if(sayi=="q"):
        print("çıkış yapılıyor..")
        break
    
    else:
        sayi=int(sayi)
        faktöriyel=1
        
        for i in range(2,sayi+1):
            faktöriyel*=i
        print("faktöriyeli:",faktöriyel)
                
    