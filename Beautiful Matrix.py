n={}
for I in range (1,6):
    b=list (map(int, input(). split()))
    if 1 in b:
        n[I]=b
        c=b.index(1)+1
        x=abs(I-3)+abs(c-3)
print (x)       