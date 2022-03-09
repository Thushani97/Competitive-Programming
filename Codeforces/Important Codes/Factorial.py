def factorial(x):
    if x== 0:
        print(1)
    else:
        ans=1
        for i in range(1,x+1):
            ans=ans*i
            print(ans,i)
        return(ans)

print(factorial(5))