n=int(input())
sum=0
for i in range(n):
    p,q= list(map(int,input().split()))
    if p+2<=q:
        sum+=1
print(sum)