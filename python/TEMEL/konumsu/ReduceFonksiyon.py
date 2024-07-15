#gömülü fonk: ruduce()
#reduce(function,iterasyon yapılabilen veri tipi(liste vb))
#soldan başlayaeak listenin ilk 2 elemanına uygular sonucu 3.elemanına uygular


from functools import reduce

def toplama(x,y):
    return x+y

sonuc =reduce(toplama,[12,18,20,10])
print(sonuc)

#########################################



from functools import reduce

print(reduce(lambda x,y:x+y,[12,18,20,10]))

#########################################




#faktoriyel:

print(reduce(lambda x,y:x*y,[1,2,3,4,5]))

#########################################


def max(x,y):
    if(x>y):
        return x
    else:
        return y
    
    
print(reduce(max,(-2,3,5)))

#########################################
