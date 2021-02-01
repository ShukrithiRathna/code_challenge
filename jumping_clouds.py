#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps=0
    pos = 0 
    while pos < (len(c)-1):
        try:
            if c[pos+2]!=1:
                pos=pos+2
            else:
                pos+=1
        except(IndexError):
            pos+=1  
        jumps+=1
        print("Pos:",pos,"\nJumps:",jumps)  
    return jumps

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)