
k,n,w= list(map(int,input().split()))

sum=0
for i in range(1,w+1):
    sum+=i*k
    
if sum>n:
    print(sum-n)
else:
    print(0)