n=int(input())

lst=[]
sum=0
for i in range(n):
    d,i=(list(map(int,input().split())))
    sum=sum-d+i
    lst.append(sum)
print(max(lst))