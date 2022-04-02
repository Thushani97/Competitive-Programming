def extraLongFactorials(n):
    # Write your code here
    mul=1
    for i in range(n,0,-1):
        mul*=i
    print(mul)

n = int(input().strip())

extraLongFactorials(n)
