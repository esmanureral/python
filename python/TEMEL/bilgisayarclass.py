class Bilgisayar():
    def __init__(self,marka, model, islemci, ram, depolama):
        self.marka=marka
        self.model=model
        self.islemci=islemci
        self.ram=ram
        self.depolama=depolama
        

    
    def __str__(self):
        return "Markası: {} \n Modeli: {} \n İslemcisi: {}\n Rami: {}\n depolaması : {} \n".format(self.marka,self.model,self.islemci,self.ram,self.depolama)
   
   
    def ramartir(self,miktar):
        self.ram+=miktar
        
        
    
        
Bilgisayar1=Bilgisayar("Dell", "XPS 15", "Intel i7", 16, 512)    
print(Bilgisayar1)
print(Bilgisayar1.ramartir(8))
print(Bilgisayar1)
