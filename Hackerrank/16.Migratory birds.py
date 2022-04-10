n=int(input())
List=list(map(int,input().strip().split()))


print(max(lst,key=lst.count))

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
print(most_frequent(List))


'''
I couldn't solve this problem myself
