#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    score=0
    valley_count=0
    for step in path:
        if step == "D":
            score-=1
        if step == "U":
            score+=1
            if score == 0:
                valley_count+=1
    return valley_count    

steps = int(input().strip())
path = input()
result = countingValleys(steps, path)
print(result)