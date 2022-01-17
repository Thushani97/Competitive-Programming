n=int(input().strip())
arr =[]

for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))

list1=[]
list2=[]

for i in range (n):
    list1.append(arr[i][i])
    list2.append(arr[i][n-i-1])

print (abs(sum(list1)-sum(list2)))