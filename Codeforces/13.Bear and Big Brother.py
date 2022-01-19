L,B = list(map(int,input().split()))

sum=0
while B>=L:
    L=L*3
    B=B*2
    sum+=1

print(sum)
