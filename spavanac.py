n,m=input(). split()
n=int(n)
m=int(m)
if n==0 :
    if m==45:
        print (00,00)
    elif m>45:
        print (00,m-45)   
    elif m<45:
        b=45-m
        v=60-b
        print (23,v)  
else :
    if m==45:
        print (n,00) 
    elif m>45:
        print (n,m-45) 
    elif m<45:
        b=45-m
        v=60-b
        print (n-1,v)  