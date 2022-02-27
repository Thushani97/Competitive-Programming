for i in range(int(input())):
    a,b,c= list(map(int,input().split()))
    r= abs(a-b)
    circle=r*2
    if r>1 and c<= circle and a<= circle and b<=circle:
        if c+r<=circle:
            print (c+r)
        else:
            print(c-r)
    else:
        print(-1)

