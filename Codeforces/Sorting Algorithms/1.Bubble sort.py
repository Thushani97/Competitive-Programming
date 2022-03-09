def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return(lst)

lst=[5, 3, 8, 6, 7, 2]  
print(bubble_sort(lst))