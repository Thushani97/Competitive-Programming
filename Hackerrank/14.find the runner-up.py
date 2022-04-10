n = int(input())
arr = list(map(int, input().split()))
arr.sort()
new_arr= arr[::-1]
max_=new_arr[0]

for i in new_arr:
    if i<max_:
        print(i)
        break
    else:
        continue
