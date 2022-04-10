n=int(input())

lst=[]
for i in range(n):
    lst.append(int(input()))

ans=[]

marks=[40,45,50,55,60,65,70,75,80,85,90,95,100]
for j in lst:
    
    if j>37:
        for i in range(len(marks)):
            
            if (marks[i]-j)==3 or (marks[i]-j)==0:
                ans.append(j)
                break
            if 0<(marks[i]-j)<3:
                ans.append(marks[i])
                break
            if 5>(marks[i]-j)>3:
                ans.append(j)
                break
          
    else:
        ans.append(j)
print('\n'.join(list(map(str,ans))))
