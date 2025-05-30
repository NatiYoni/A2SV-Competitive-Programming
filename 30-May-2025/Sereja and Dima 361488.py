# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

import sys, collections, math, random, bisect

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():

    n = inp()

    arr = inlt()

    l = 0 
    r = n - 1
    s = 0
    d = 0
    flag = False
    while l <= r:
        
        if arr[l] > arr[r]:
            if not flag:
                s += arr[l]
            else:
                d += arr[l]
            
            l += 1
        else:
            if not flag:
                s += arr[r]
            else:
                d += arr[r]
            
            r -= 1
        flag = not flag 

    print(s,d)
        
    pass

def main():
    multi = False # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()