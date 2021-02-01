#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    sub_count=s.count('a')
    sub_len=len(s)
    rep_num=int(n/sub_len)
    remaining_string = n%sub_len

    count=sub_count*rep_num
    if remaining_string:
        count+=s[0:remaining_string].count('a')
    return count    

if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)

