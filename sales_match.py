#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    temp_stack = []
    count = 0 
    ar.sort()
    temp_stack.append(ar.pop(0))
    while ar:
        temp=ar.pop(0)
        if temp_stack and temp==temp_stack[-1]:
            count+=1
            temp_stack.pop(-1)
        else:
            temp_stack.append(temp)  
    return(int(count))

n = int(input())
ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print(result)