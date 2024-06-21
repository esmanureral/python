""" Beden Kitle İndeksi:Kilo/Boy(m)*Boy(m)
BKİ 18.5'un altındaysa -------> Zayıf
BKİ 18.5 ile 25 arasındaysa ------> Normal
BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
BKİ 30'un üstündeyse -------------> Obez
"""

print("BEDEN KİTLE İNDEKSİ HESAPLAMA")

kilo=int(input("Kilonuzu giriniz:"))
boy=float(input("Boyunuzu giriniz:"))

bki=kilo/(boy**2)

if (bki < 18.5):
    print("Zayıf")
elif (bki >= 18.5 and bki < 25):
    print("Normal")
elif (bki >= 25 and bki < 30):
    print("Fazla Kilolu")
else:
    print("Obez")
5