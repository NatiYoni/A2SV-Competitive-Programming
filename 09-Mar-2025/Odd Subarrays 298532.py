# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))


# Defaultdict for handling missing keys automatically
def dd_int():
    return collections.defaultdict(int)
def dd_list():
    return collections.defaultdict(list)
def dd_set():
    return collections.defaultdict(set)

def is_in_bounds(grid, i, j):
   return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():

    n = inp()
    arr = inlt()

    count = 0
    index = 1
    while index < n:

        if arr[index-1] > arr[index]:
            count += 1
            index += 1

        index += 1

    
    print(count)

def main():
    multi = True # if multiple Test cases change it to true
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()