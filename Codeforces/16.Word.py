n=input()
sum1=0
sum2=0

for i in n:
    if i.islower(): # i.islower--> to check whether the character is lower
        sum1+=1
    else:
        sum2+=1

if sum1>=sum2:
    print(n.lower())
else:
    print(n.upper())