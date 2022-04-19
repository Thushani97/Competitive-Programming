for i in range(int(input())):
    k=int(input())
    sum_=0
    lst= list(map(int,input().split()))
    if sum(lst) >=len(lst):
        print(sum(lst)-len(lst))
    elif (sum(lst)<0 or sum(lst)<k):
       
        print (1)
 