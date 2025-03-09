# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    # solution here
    n, k  =  invr()
    arr = inlt()
    

    if n == k:
        print(0)
        return
    
    # right = n - 1
    # left = n - k
    # min_ = arr[left] - arr[0]
    

    
    # while left > 0:
        
    #     min_ = min(min_,arr[left]-arr[0] + arr[n - 1] - arr[right]) 
    #     # print(arr[left]-arr[0])
    #     # print(arr[n - 1] - arr[right])
    #     left -= 1
    #     right -= 1

    

        
    
    # print(min_)

    diff = [0] * (n - 1)
    sum_ = 0

    for i in range(1,n):
        diff[i-1] = arr[i] - arr[i-1]
    
    diff.sort()
    for i in range(n-k):
        sum_ += diff[i]

    print(sum_)
    pass

def main():
    multi = False # if multiple Test cases change it to true
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()