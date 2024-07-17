"""
Elinizden her bir elemani 3'lü bir demet olan bir liste olsun.
     [(3,4,5),(6,8,10),(3,10,7)]
Şimdi kenar uzunluklarina göre bu kenarlarin bir üçgen olup olmadiğini 
dönen bir fonksiyon yazin ve sadece üçgen belirten kenarlari bulunduran listeyi ekrana yazdirin.
     [(3, 4, 5), (6, 8, 10)]
"""


def üçgenmi(demet):
     if (abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]):
         return True
     else:
         return False
     
liste=[(3,4,5),(6,7,8),(3,10,7)]

print(list(filter(üçgenmi,liste)))