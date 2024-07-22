"""
Elinizde "mailler.txt" adında, 
maillerin ve bazı yazıların bulunduğu bir dosya olsun.
Bu dosyanın her bir satırını okuyun ve sadece mail formatına
uygun olanları ekrana yazdırın.

"""

with open("mailler.txt","r",encoding="utf-8")as file:
    for satır in file:
        satır=satır[:-1]#her satırın sonunda yer alan newline (\n) karakterini kaldırır.
        if(satır.endswith(".com") and satır.find("@")!=-1):
            print(satır)
        
    """
    if (satır.endswith(".com") and satır.find("@") != -1)
    bir satırın hem ".com" ile bitip bitmediğini 
    hem de içinde "@" karakterini içerip içermediğini kontrol eder.
   
   satır.find("@") != -1: belirtilen karakteri bulursa karakterin ilk geçtiği pozisyonu döner; bulamazsa -1 döner. 
   
    """