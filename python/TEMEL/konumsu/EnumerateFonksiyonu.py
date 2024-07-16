#İndexlerle Numaralandırma 

liste=["Elma","Armut","Muz","Kiraz"]
sonuç=list()
i=0
for a in liste:
    sonuç.append((i,a))
    i+=1
print(sonuç) #[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]


#ya da

liste=["Elma","Armut","Muz","Kiraz"]
i=0
sonuç=list()

while(i<len(liste)):
    sonuç.append((i,liste[i]))
    i+=1
print(sonuç) #[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')] 


#####################################################


liste=["Elma","Armut","Muz","Kiraz"]

print(list(enumerate(liste))) ##[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')] 



##ÇİFT İndex  OLANLARI BASTIRMA

liste=["a","b","c","d","e","f","g"]
for i,j in enumerate(liste):
    if(i%2==0):
        print(j)