n=list(input())

sum=0
for i in n:
    if i =='4' or i=='7':
        sum+=1 
if sum==7 or sum==4:
    print("YES")
else:
    print("NO")
