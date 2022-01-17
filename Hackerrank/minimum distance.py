n=int(input())
lst= list(map(int, input().strip().split()))

ans=[]
for i in range (n):
    for j in range (n):
        if lst [i]==lst[j] and i!=j and i<j:
            ans.append(j-i)
        
if ans==[]:
    print (-1)
else:
    print(min(ans))
