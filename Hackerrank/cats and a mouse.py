n=int(input())

for i in range (n):
    x,y,z=list(map(int,input().strip().split()))
    if abs(x-z)==abs(y-z):
        print("Mouse C")
    elif abs(x-z)>abs(y-z):
        print ("Cat B")
    elif abs(x-z)<abs(y-z):
        print ("Cat A")
    
