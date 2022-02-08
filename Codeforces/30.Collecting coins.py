for i in range(int(input())):
    lst= list(map(int,input().split()))
    n=lst.pop()
    index_=lst.index(max(lst))
    max_ = lst.pop(index_)
    print(n,index_,max_,lst)