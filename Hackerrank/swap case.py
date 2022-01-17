def swap_case(s):
    n=list(s)
    lst=[]
    for i in n:
        
        if (i.isupper()):
            lst.append(i.lower())
        elif(i.islower()):
            lst.append(i.upper())
        else:
            lst.append(i)
    result=("".join(lst))
    return result
s=input()
result = swap_case(s)
print(result)
