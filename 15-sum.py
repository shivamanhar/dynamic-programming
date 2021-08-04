#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total_length = len(arr)
    total_plus = float(0)
    total_minus = float(0)
    total_zero =float(0)
    for i in range(total_length):
        if arr[i] >= 1:
            total_plus = total_plus+1
        if arr[i] < 1 and arr[i] != 0:
            total_minus = total_minus+1
        if arr[i] == 0:
            total_zero = total_zero+1
    
    if total_plus != 0:
        print('{:.6f}'.format(total_plus/total_length))
    else:
        print('{:.6f}'.format(total_plus))
    if total_minus != 0:
        print('{:.6f}'.format(total_minus/total_length))
    else:
        print('{:.6f}'.format(total_minus))
    if total_zero != 0:
        print('{:.6f}'.format(total_zero/total_length))
    else:
        print('{:.6f}'.format(total_zero))
        
    # Write your code here

if __name__ == '__main__':
    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
