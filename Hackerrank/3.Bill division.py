n,index=list(map(int,input().split()))

lst=list(map(int,input().strip().split()))
b_charged = int(input())

lst.pop(index)
b_actual=(sum(lst)//2)

if b_charged-b_actual==0:
    print("Bon Appetit")
else:
    print(b_charged-b_actual)
