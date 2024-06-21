#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

a=int(input("enter the first number "))
b=int(input("enter the second number:"))
c=int(input("enter the third number"))
product=a*b*c

print("The result of the operation:  {}".format(product))

####
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

çarpım = a * b * c

print("{} x {} x {} = {} dir".format(a,b,c,çarpım))