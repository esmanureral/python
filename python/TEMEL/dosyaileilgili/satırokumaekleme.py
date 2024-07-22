#dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek
# bir string oluşturun ve bu string'i ekrana yazdırın.

basharf=""

with open("şiir.txt","r",encoding="utf-8")as file:
    for satır in file:
        basharf+=satır[0] #her satırın ilk harfi alınır
print(basharf)