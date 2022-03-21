for i in range(int(input())):
    a,b = list(map(int,input().split()))
    area = 2*a*b
    root=area**0.5
    if root== float(a) or root==float(b):
        print(int(root))
    else:
        value=int(root)
        print(value* value)