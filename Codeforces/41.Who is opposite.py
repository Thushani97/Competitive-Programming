for i in range(int(input())):
    a,b,c= list(map(int,input().split()))
    r= abs(a-b)
    circle=r*2
    if r>1 and c+r<= circle:
        print (c+r)
    else:
        print(-1)

