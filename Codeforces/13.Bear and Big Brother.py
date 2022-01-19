L,B = list(map(int,input().split()))# input --> 4 7 --> [4,7]

sum=0
while B>=L:
    L,B=L*3,B*2
    sum+=1

print(sum)
