n,t= list(map(int,input().split()))
q=input()

for i in range(t-1):
    if q[i]<q[i+1]:
        q[i],q[i+1]=q[i+1],q[i]
        print(q)