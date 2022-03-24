for i in range(int(input())):
    a,b = list(map(int,input().split()))
    area = 2*a*b
    root=area**0.5
    if root== float(a) or root==float(b):
        print(int(root)*int(root))
    else:
        value=int(root)+1
        print(value* value)


# Correct answer
# t=int(input())
# for i in range(t):
#     l=list(map(int,input().split()))
#     a=l[0]
#     b=l[1]
#     if(a!=b and (2*a<b or 2*b<a)):
#         if(2*a<b):
#             print(b**2)
#         elif(2*b<a):
#             print(a**2)
#     else:
#         if(2*a<=2*b):
#             print((2*a)**2)
#         else:
#             print((2*b)**2)
