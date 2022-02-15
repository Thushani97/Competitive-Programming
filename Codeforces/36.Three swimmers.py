for i in range(int(input())):
    lst=list(map(int,input().split()))
    p=lst.pop(0)
    if p in lst:
        print (0)
    elif p> max(lst):
        j=2
        while True:
            lst=[i*j for i in lst]
            j+=1
            ans=[]
            for i in lst:
                if p<i:
                    ans=[i-p for i in lst]
                    print (abs(min(ans)))
                    break
                else:
                    pass
            break
               
    else:
        print (min(lst)-p)