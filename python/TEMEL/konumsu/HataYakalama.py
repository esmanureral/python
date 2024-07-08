
"""
    try:

        Hata çıkarabilecek kodlar buraya yazılıyor.
        Eğer hata çıkarsa program uygun olan except bloğuna girecek.
        Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
        except Hata1:
            Hata1 oluştuğunda burası çalışacak.
        except Hata2:
            Hata2 oluştuğunda burası çalışacak.
            
    finally:
    mutlaka çalışacak blok
"""
    
    #1
try:
    a=int("sssdf23")
    print("program burada ")
except:
    print("bir hata oluştu")
print("bloklar sona erdi")

# 1 = ssdf23 kısmı hata verir valuerror, hata verdiği için direkt excepte girer devam eder.


    #2
try:
    a=int("23")
    print("program burada")
except:
    print("bir hata oluştu")
print("bloklar sona erdi")
    
# 2 = 23 kısmı hata vermeyeceği için excepte girmeden sırayla çalışır.