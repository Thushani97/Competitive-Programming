for i in range(int(input())):
    x,y,n = list(map(int,input().split()))
    
    print(n-(n-y)%x)