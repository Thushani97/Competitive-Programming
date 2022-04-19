for i in range(int(input())):
    k=int(input())
    lst= list(map(int,input().split()))
    if sum(lst) >=len(lst):
        print("ans",sum(lst)-len(lst))
    else:
        
    #print(abs(k-(sum(lst))))