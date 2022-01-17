x=(input())
y=(input())

a=list(x.lower())
b=list(y.lower())


for i in range(len(a)):
    if a!=b:
        if a[i]>b[i]:
            print("1")
            break
        elif a[i]<b[i]:
            print("-1")
            break
    else:
        print("0")
        break



    

