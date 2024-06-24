
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




#daha gelişmiş hali

syskullaniciadi = "esmanur"
sysparola = "esmanur123"
girişhakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    parola = input("Parola: ")

    if kullanici_adi != syskullaniciadi and parola == sysparola:
        print("Kullanıcı adı hatalı")
        girişhakki -= 1
    elif kullanici_adi == syskullaniciadi and parola != sysparola:
        print("Parola hatalı")
        girişhakki -= 1
    elif kullanici_adi != syskullaniciadi and parola != sysparola:
        print("Kullanıcı adı ve parola hatalı")
        girişhakki -= 1
    else:
        print("Başarıyla giriş yaptınız!")
        break

    if girişhakki == 0:
        print("Giriş hakkınız bitti.")
        break