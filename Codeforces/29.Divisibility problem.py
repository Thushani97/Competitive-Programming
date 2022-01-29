

for i in range(int(input())):
    n,d=list(map(int,input().split()))
    if n%d==0:
        print(0)
    else:
        sum=0
        while True:
            if (n%d)!=0:
                n+=1
                sum+=1
                
            elif n %d==0:
                print(sum)
                break