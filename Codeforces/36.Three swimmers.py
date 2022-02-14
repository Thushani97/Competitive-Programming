for i in range(int(input())):
    lst=list(map(int,input().split()))
    p=lst.pop(0)
    print(lst)
    if p in lst:
        print (0)
  