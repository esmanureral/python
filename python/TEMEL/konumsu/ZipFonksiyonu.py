#LİSTE GRUPLANDIRMAK İSTESEK

list1=[1,2,3,4,5]
list2=[6,7,8,9,10,11]

i=0
sonuc=list()
while(i<len(list1) and i<len(list2)):
    sonuc.append((list1[i],list2[i]))
    i+=1
print(sonuc) #[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]




#BUNU ZİPLE YAPABİLİRİZZ

list1=[1,2,3,4,5]
list2=[6,7,8,9,10,11]
print(list(zip(list1,list2)))



#AYNI ANDA İKİ LİSTE ÜZERİNDE GEZİNEBİLİRİZ

list1=[1,2,3,4]
list2=["Python","Php","Java","C#"]

for i,j in zip(list1,list2):
    print("i:",i,"j:",j)
    
    
#########################################

sözlük1={"Elma":1,"Armut":2,"Kiraz":3}
sözlük2={"Sıfır":0,"Bir":1,"İki":2}
print(list(zip(sözlük1,sözlük2))) #[('Elma', 'Sıfır'), ('Armut', 'Bir'), ('Kiraz', 'İki')]

print(list(zip(sözlük1.values(),sözlük2.values())))#[(1, 0), (2, 1), (3, 2)]