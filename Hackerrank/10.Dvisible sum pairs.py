n,k = list(map(int,input().strip().split()))
lst=list(map(int,input().strip().split()))

ans=[]
for i in range (len(lst)):
    for j in range (len(lst)):
        if i != j and i<j and (lst[i]+lst[j])%k==0:
            ans.append(lst[i]+lst[j])

print (len(ans))
