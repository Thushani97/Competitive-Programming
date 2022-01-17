x,y,z= input().split(':')
a,b= int(x), int(y)
c=int(z[0:2])
d=z[0:2]
t= z[2:]
if t== 'AM':
    if a==12:
        print("00"+':'+y+':'+d)
    else:
        print(x+':'+y+':'+d)
else:
    if a==12:
        print("12"+':'+y+':'+d)
    else:
        f=str(a+12)
        print(f+':'+y+':'+d)
