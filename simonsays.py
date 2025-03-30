n=int(input ())
for I in range (n):
    n=list(input (). split())
    if n[0]=='Simon' and n[1]=='says':
        n.remove('Simon')
        n.remove('says')
        for I in n:
            print (I,end=' ')