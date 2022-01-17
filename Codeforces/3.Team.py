n= int(input())
sum=0
for i in range(n):
    lst=(input().split(" "))
    
    count= lst.count("1")
    #print("count %d"%count)
    if count>=2:
        sum+=1
    else:
        pass
print (sum)