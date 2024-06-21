print("""***************************
      HESAP MAKİNESİ
      1.TOPLAMA İŞLEMİ
      2.ÇIKARMA İŞLEMİ
      3.ÇARPMA İŞLEMİ
      4.BÖLME İŞLEMİ
***************************""" )

a=int(input("Birinci sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
islem=input("istenilen işlemi giriniz:")

if islem =="1":
    print("{} ile {} nin toplamı: {}".format(a,b,a+b))
elif islem=="2":
    print("{} ile {} nin farkı: {}".format(a,b,a-b))
elif islem=="3":
    print("{} ile {} nin çarpımı: {}".format(a,b,a*b))
elif islem=="4":
    print("{} ile {} nin bölümü: {}".format(a,b,a/b))
else:
    print("geçersiz bir ifade girdiniz.")
    
    
    
