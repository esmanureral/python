#gömülü fonk: map()
#map(fonksiyon,iterasyon yapılabilecek veri tipi (liste,demet..))



def double(x):
    return x *2

map(double,[1,2,3,4,])
print(list(map(double,[1,2,3,4,])))

#########################################

print(list(map(lambda x:x**2,(1,2,3,4,5)))) #kare alma

#########################################

list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[9,10,11,12,13]

print(list(map(lambda x,y:x*y,list1,list2)))

#########################################

list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[9,10,11,12,13]

print(list(map(lambda x,y,z:x*y*z,list1,list2,list3)))

list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[9,10,11,12,13]

print(list(map(lambda x,y:x*y,list1,list2)))