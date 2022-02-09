for i in range(int(input())):
    x,y,n = list(map(int,input().split()))
    if n%x == y:
        print(n)
    elif n<x:
        print(0)
    elif y==0:
        a= n//x
        print(a*x)