n,k=list(map(int,input().strip().split()))
lst=list(map(int,input().strip().split()))

if max(lst)>k:
    print(max(lst)-k)
else:
    print(0)
