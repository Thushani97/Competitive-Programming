for i in range(int(input())):
    p, a, b, c = list(map(int,input().split()))
    print(min(-p % a, -p % b, -p % c))