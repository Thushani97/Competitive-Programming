
for i in range(int(input())):
    n= int(input())
    a=n//3
    
    c=(a+1)
    d= (a+2)
    e=a+1
    if a + (a*2) == n : 
        print(a,a)
    elif a+c*2==n:
        print(a,c)
    elif a+d*2==n:
        print(a,d)
    elif   e+a==n:
        print(e,a)
