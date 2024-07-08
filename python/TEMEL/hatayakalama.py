"""
liste = ["345","sadas","324a","14","kemal"]
Bu listenin içindeki stringlerden içinde sadece rakam bulunanlari ekrana yazdirin. Bunu yaparken try,except bloklarini kullan.
"""

liste=["345","sadas","324a","14","kemal"]

for i in  liste:
    try:
        i=int(i)
        print(i)
    except:
        pass
    
    
"""
Bir sayinin çift olup olmadiğini sorgulayan bir fonksiyon yaz
Bu fonksiyon, eğer sayi çift ise *return* ile bu değeri dönsün. 
Ancak sayi tek sayi ise fonksiyon *raise* ile *ValueError* hatasi firlatsin. 
Daha sonra,içinde çift ve tek sayilar bulunduran bir liste tanimlayin ve liste üzerinde gezinerek ekrana sadece çift sayilari bastirin.
"""

def çifttek(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError
liste = [34,2,1,3,33,100,61,1800]
for i in liste:
    try:
        print(çifttek(i))
    except ValueError:
     pass
    
    