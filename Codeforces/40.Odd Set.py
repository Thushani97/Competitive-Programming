for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    even=0
    odd=0
    for j in lst:
        if j%2==0:
            even+=1
        else:
            odd+=1

    if even==odd:
        print("YES")
    else:
        print("NO")