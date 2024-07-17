"""
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayilarin toplamini ekrana yazdiran bir fonksiyon yazin.

*Not: İlk önce filter() fonksiyonu ile çift sayilari ayiklayin.
Daha sonra reduce() fonksiyonunu kullanin.
"""

from functools import reduce
liste=[1,2,3,4,5,6,7,8,9,10]
filtre=list(filter(lambda x:x%2==0,liste))
print(reduce(lambda x,y:x+y,filtre))


