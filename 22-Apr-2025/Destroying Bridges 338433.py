# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

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

    n, k = invr()
    temp = n - 1

    if k >= n - 1:
        print(1)
        return 
    
    print(n)
    
    # while k >= 0:
    #     k -= (n-1)
    #     n -= 1
    
    # if k == 0:
    #     print(n)
    # else:
    #     print(n+1)
    # pass

def main():
    multi = True  
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()