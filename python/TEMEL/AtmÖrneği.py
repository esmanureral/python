print(""" ******************************** 
      
      ATM MAKİNESİNE HOŞGELDİNİZ
      
      1-BAKİYE SORGULAMA
      2-PARA YATIRMA
      3-PARA ÇEKME
      programdan çıkmak için q ya basınız.
      
      """)

bakiye=1000

while  True:
    
    işlem=input("Seçmek istediğiniz işlem:")
    
    if(işlem=="q"):
        print("çıkış yaptınız..")
        break
    elif(işlem=="1"):
        print("Bakiyeniz {} TL dir.".format(bakiye))
        
    elif(işlem=="2"):
        yatirilacaktutar=int(input("Yatırmak istediğiniz miktarı giriniz:"))
        bakiye=bakiye+yatirilacaktutar
        
    elif(işlem=="3"):
        çekilecekmiktar=int(input("Çekmek istediğiniz miktarı giriniz:"))
        if(çekilecekmiktar>bakiye):
            print("Yetersiz Bakiye")
            continue
        bakiye=bakiye-çekilecekmiktar
        
        
    else:
        print("geçersiz işlem")
        
    
    
    


