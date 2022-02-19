for i in range(int(input())):
    n,m= list(map(int,input().split()))
    m=float(m)
    lst=sorted(list(map(int,input().split())))
    sum=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            sum+= lst[j-1]/j
    
    if sum==m:
        print("YES")
    else:
        print("NO")