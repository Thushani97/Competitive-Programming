for i in range(int(input())):
    a,b= list(map(int,input().split()))
    sub = abs(a-b)
    if sub%10 ==0:
        print(sub//10)
    else:
        print(sub//10 +1)