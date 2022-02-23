for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    sum=0
    for i in lst:
        if i+1 in lst:
            print("ans",2)
            break
    else:
        print("ans",1)