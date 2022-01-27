ans=[]
for i in range(int(input())):
    n,m=list(map(int,input().split()))
    if (m+1)%2==0:
        ans.append(str((m//2)*n+(n+1)//2))
    elif ((m+1)%2==1):
        ans.append(str((m//2)*n))

print("\n".join(ans))
