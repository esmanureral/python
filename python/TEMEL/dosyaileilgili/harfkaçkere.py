#"ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
#Bu string içindeki harflerin frekansını 
#(bir harfin kaç defa geçtiği) bulmaya çalışın.



s="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans=dict()

for karakter in s:
    if(karakter in frekans):
        frekans[karakter]+=1
    else:
        frekans[karakter]=1

for i,j in frekans.items():
    print(i ,":",j)