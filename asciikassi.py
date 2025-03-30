n=int(input())      
if n==0:
    print ('++')
    print ('++')
else:
   print('+'+n*'-'+'+')
   for p in range (n):
       print ('|'+n*' '+'|')
   print('+'+n*'-'+'+') 
 