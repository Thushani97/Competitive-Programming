for i in range(int(input())):
    n,m= list(map(int,input().split()))
    # m=float(m)
    lst=sum(list(map(int,input().split())))
    # print(lst)
    # sum=0
    # for i in range(1,n+1):
        # for j in range(i,n+1):
            # print(lst[j-1],j)
            # sum+= lst[j-1]/j
    
    if lst==m:
        print("YES")
    else:
        print("NO")