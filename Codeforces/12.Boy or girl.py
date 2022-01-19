lst=list(input()) # list an inpput string
original_lst=set(lst) # To delete the repetitive letters in a string
if len(original_lst)%2==1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")