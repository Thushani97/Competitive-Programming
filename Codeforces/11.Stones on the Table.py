n=int(input())
lst=list(input())
sum=0
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        sum+=1
print (sum)