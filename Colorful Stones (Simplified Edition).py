s = input().strip()
m = input().strip()
p = 0
 
for c in m:
    if p < len(s) and s[p] == c:
        p += 1
 
print(p + 1)