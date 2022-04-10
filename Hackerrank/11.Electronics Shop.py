b,n,m = list(map(int,input().strip().split()))
keyboards=list(map(int,input().strip().split()))
drives=list(map(int,input().strip().split()))

ans=[]
for i in range (n):
    for j in range (m):
        if (keyboards[i]+ drives[j])<=b:
            ans.append(keyboards[i]+drives[j])

if ans==[]:
    print (-1)
else:
    print(max(ans))
