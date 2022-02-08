for i in range(int(input())):
    lst= list(map(int,input().split()))
    n=lst.pop()
    index_=lst.index(max(lst))
    max_ = lst.pop(index_)

    for i in lst:
        n=n-(max_-i)


    if n>=0 and n%3 ==0:
        print("YES")
    else:
        print("NO")
    