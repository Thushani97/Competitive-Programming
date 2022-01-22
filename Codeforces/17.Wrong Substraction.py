n,k=input().split()
integ = int(n)
itt =int(k)

for i in range(itt):
    if n[-1]!="0":
        integ= integ-1
        n=str(integ)
        
    else:
        integ=integ//10
        n=str(integ)
      

print(n)

