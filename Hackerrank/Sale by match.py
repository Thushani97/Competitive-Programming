n=(int(input()))
ar = list(map(int,input().split()))
dic={}

for i in ar:
    dic[i]= (ar.count(i))//2
   
return(sum(dic.values()))