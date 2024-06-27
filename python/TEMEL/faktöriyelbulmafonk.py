def faktoriyel(sayi):
    faktoriyel=1
    if(sayi==0 or sayi==1):
        print("faktöriyel:",faktoriyel)
    
    else:
        while(sayi>1):
            faktoriyel*=sayi
            sayi-=1
            
        print("faktoriyel:",faktoriyel)
            
faktoriyel(3)