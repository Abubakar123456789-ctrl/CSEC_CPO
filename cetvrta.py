k=[]
l=[]
for I in range (3):
    n, m=map(int,input (). split())
    l.append(n)
    k.append(m)
for I in l:
    for h in k:
      if  l.count(I)==1 and k.count(h)==1:  
        print (I,h) 
        break 