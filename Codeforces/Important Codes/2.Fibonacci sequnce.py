def fibonacci_sequence(n):
    if n<=2:
        print(1)
    else:
        a,b= 0,1
        for i in range(2,n):
            sum=a+b
            a=b
            b=sum
            print(sum)

(fibonacci_sequence(10))