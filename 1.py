#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    d={}
    for i in ar:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    sum = 0
    for i in d:
        if d[i]>1:
            sum += d[i]//2
    return sum
    

if __name__ == '__main__':
    fptr = open(os.environ['a.txt'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
