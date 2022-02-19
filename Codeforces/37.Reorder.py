for i in range(int(input())):
    n,m= list(map(int,input().split()))
    lst=sorted(list(map(int,input().split())))
    print(lst)
    sum=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            sum+= lst[j-1]/j
    print(sum)