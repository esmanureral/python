"""
Elinizde bir dikdörtgenin kenarlarini ifade eden sayi çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarina göre dikdörtgenin alanini hesaplayan bir fonksiyon yazin 
ve bu listenin her bir elemanina bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdirin.

         [12, 30, 30, 9]
"""


def alanhesabi(demet):
    return demet[0]*demet[1]
liste=[(3,4),(10,3),(5,6),(1,9)]
print(list(map(alanhesabi,liste)))
#[12, 30, 30, 9]