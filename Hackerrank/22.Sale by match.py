import math
import os
import random
import re
import sys


# def sockMerchant(n, ar):
    # Write your code here
n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

dic={}

for i in ar:
    dic[i]= (ar.count(i))//2 #this automatically create a dictionary
print (dic)
print(sum(dic.values()))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
