
x1,v1,x2,v2=list(map(int,input().split()))

if x1<x2 and v2>=v1:
    print ("NO")
else:
    while x1<x2:
        x1+=v1
        x2+=v2
        if x1==x2:
            print("YES")
        elif x1>x2:
            print("NO")

'''
def kangaroo(x1, v1, x2, v2):
    if v1>v2:
        while x1<x2:
            x1+=v1
            x2+=v2
    return "YES" if x1==x2 else "NO"

x1,v1,x2,v2 = map(int,input().split())
result = kangaroo(x1, v1, x2, v2)
print(result)
'''
