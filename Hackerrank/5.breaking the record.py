n=int(input())
lst=list(map(int, input().strip().split()))

best=[]
worst=[]
worst.append(lst[0])
best.append(lst[0])

for i in range (n-1):
    
    if lst[i]<lst[i+1] and lst[i+1]>max(best):
        best.append(lst[i+1])
        
    elif lst[i]>lst[i+1] and lst[i+1]<min(worst): 
        worst.append(lst[i+1])
        
print (len(best)-1 , len(worst)-1)

