# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code 
    for i in range(n-1):
        j = i + 1
        temp = arr[j]
        while arr[i] > temp and j > 0: 
            arr[j] = arr[i]
            
            j -= 1
            i -= 1
            print(*arr)
            if arr[i] < temp or j == 0:
                arr[j] = temp
                
    print(*arr)
            
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
