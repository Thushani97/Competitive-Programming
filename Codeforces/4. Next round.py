n,k= list(map(int,input().split()))
lst=list(map(int,input().split()))
# lst=list(map(int,input().strip().split()))
num=lst[k-1]

sum=0
for i in range(n):
    if lst[i]>=num and lst[i]!=0:
        sum+=1
    else:
        pass
print(sum)