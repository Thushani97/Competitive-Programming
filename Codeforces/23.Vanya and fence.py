n,h=list(map(int,input().split()))
lst=list(map(int,input().split()))

sum=0
for i in lst:
    if i>h:
        sum+=2
    else:
        sum+=1

print(sum)