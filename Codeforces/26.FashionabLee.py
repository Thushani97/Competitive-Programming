n=int(input())
ans=[]
for i in range(n):
    p=int(input())
    if p%4==0:
        ans.append("YES")
    else:
        ans.append("NO")

print("\n".join(ans))