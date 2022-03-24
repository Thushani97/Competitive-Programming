for i in range(int(input())):
    n=list(map(int,input()))
    size=[1,2,3,4]
    if n[0]>1:
        print(10*(n[0]-1)+sum(size[0:len(n)]))
    else:
        if len(n)==1:
            print(1)
        elif len(n)==2:
            print(3)
        elif len(n)==3:
            print(6)
        else:
            print(10)
    