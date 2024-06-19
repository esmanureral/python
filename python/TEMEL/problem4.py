#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a=input("birinci sayı")
b=input("ikinci sayı")
print("değişmeden önceki hali: {} {}".format(a,b))
a,b=b,a
print("değiştikten sonraki hali: {} {}".format(a,b))