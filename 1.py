#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    m=''
    k1 = k
    if k1>26:
        k=k1%26
    else:
        k=k1
    for i in s:
        if i.isalpha():
            if 65<=(ord(i)+k)<=90 or 97<=(ord(i)+k)<=122:
                m+=chr(ord(i) + k)
            elif (ord(i) +k) <65 and 65<=ord(i)<=90:
                m+=chr(ord(i) + k+26)
            elif (ord(i) +k) >90 and 65<=ord(i)<=90:
                m+=chr(ord(i) + k-26)
            elif (ord(i) +k) <65 and 97<=ord(i)<=122:
                m+=chr(ord(i) + k+26)
            elif (ord(i) +k) >90 and 97<=ord(i)<=122:
                m+=chr(ord(i) + k-26)
        else:
            m+=i
    return m

if __name__ == '__main__':
    fptr = open('a.txt', 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
