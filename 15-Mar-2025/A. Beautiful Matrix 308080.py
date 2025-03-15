# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    return list(input().strip())
def invr():
    return map(int, input().split())

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
    
    arr = [inlt() for i in range(5)]
    
    r = c = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 1:
                r = i + 1
                c = j + 1
    
    
    print(abs(3 - r) + abs(3 - c))
    pass

def main():
    multi = False 
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()