leg=int(input())

for i in range(leg):
    n,k=list(map(int,input().strip().split()))
    lst=list(map(int,input().strip().split()))
    on_time=0
    late=0
    for j in lst:
        if j<=0:            
            on_time+=1
        elif j>0:
            late+=1
     
    if on_time >=k:
        print("NO")
    else:
        print("YES")
