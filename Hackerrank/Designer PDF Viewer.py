lst=list(map(int,input().strip().split()))
name=list(input())
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

index=[]
for i in name:
    (index.append(alphabet.index(i)))

value=[]
for j in index:
    value.append(lst[j])

print(max(value)*len(name))

