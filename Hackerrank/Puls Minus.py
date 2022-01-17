n=int(input())
lst=list(map(int,input().strip().split()))

negative=[]
postive=[]
zero=[]
for i in lst:
    if i<0:
        negative.append(i)
    elif i==0:
        zero.append(i)
    else:
        postive.append(i)

a=(len(postive)/n)
b=(len(negative)/n)
c=(len(zero)/n)

###  Get 6 decimal values ###
print("{:.6f}".format(round(a, 6)))
print("{:.6f}".format(round(b, 6)))
print("{:.6f}".format(round(c, 6)))
