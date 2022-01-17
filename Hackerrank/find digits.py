inputLines = int(raw_input())
for i in range(inputLines):
    total = 0
    number = int(raw_input())
    temp = number
    while number > 0:
        if number%10 != 0 and temp%(number%10)==0:
            total += 1
        number /= 10
    print total
