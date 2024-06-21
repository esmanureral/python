print("Kullanıcı Girişi")

syskullaniciadi="Esmanur"
syskullanicisifre="Esmanur123"

kullanici_adi=input("Kullanıcı Adınızı Giriniz:")
kullanici_sifre=input("Şifrenizi Giriniz:")


if(kullanici_adi==syskullaniciadi and syskullanicisifre!=kullanici_sifre):
    print("şifrenizi hatalı girdiniz.")
    
elif(kullanici_adi!=syskullaniciadi and kullanici_sifre==syskullanicisifre):
    print("kullanıcı adınızı hatalı girdiniz")

elif(kullanici_adi!=syskullaniciadi and syskullanicisifre!=kullanici_sifre):
    print("kullanıcı adınızı ve şifrenizi hatalı girdiniz")
    
else:
    print("giriş yapıldı")




