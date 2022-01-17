lst= list(map(int, input().strip().split()))

add=[]
for i in range(len(lst)):
    add.append(sum(lst[0:i]+lst[i+1:]))


print(min(add),max(add))
