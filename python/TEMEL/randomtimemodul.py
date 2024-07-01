import random #rastgele sayı
import time #bir sny beklemek için

print(" *** 1 ile 40 arasında sayıyı tahmin edin ***")


rastgelesayı=random.randint(1,40)
tahminhakki=7

while True:
    tahmin=int(input("tahmininiz:"))
    if(tahmin<rastgelesayı):
        print("sorgulanıyor..")
        time.sleep(1)
        print("daha yüksek sayı soyleyınız.")
        tahminhakki-=1
    elif(tahmin>rastgelesayı):
        print("sorgulanıyor..")
        time.sleep(1)
        print("daha düşük sayı soyleyınız.")
        tahminhakki-=1
    else:
        print("sorgulanıyor..")
        time.sleep(1)
        print("tebrikler",rastgelesayı)
        break
    
    if(tahminhakki==0):
        print("tahmin hakkınız bitti")
        print("sayınız:",rastgelesayı)
        break
        
        
        
