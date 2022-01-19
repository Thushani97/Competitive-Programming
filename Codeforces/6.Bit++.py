n=int(input())

ans=[]
for i in range(n):
    lst=list(input())

    for i in lst:
        if i== "+":
            ans.append(1)
        elif i=="-":
            ans.append(-1)
        else:
            pass
print(sum(ans)//2)