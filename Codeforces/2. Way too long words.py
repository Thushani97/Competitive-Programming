import string


n=int(input())

lst=[]
for i in range(n):
    item= list(input())
    if len(item)<=10:
        lst.append("".join(item))
    else:
        middle_len= len(item)-2
        lst.append(item[0]+"%d"%middle_len+item[len(item)-1])

print("\n".join(lst))
