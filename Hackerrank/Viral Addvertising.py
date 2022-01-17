n=int(input())

linked_0= 5//2
lst=[linked_0]
for i in range(n-1):
    linked= lst[i]*3
    lst.append(linked//2)
print(sum(lst))