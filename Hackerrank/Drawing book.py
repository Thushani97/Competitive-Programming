n=int(input())
p=int(input())

pages= (n//2)+1
need= (p//2)+1

if pages%2==0:
    m=(pages//2)+0.5
    print(m)
 
else:
    m=(pages//2)+1


if need<m:
   
    print(need-1)
    
else:
    print(pages-need)
