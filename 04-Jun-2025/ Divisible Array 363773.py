# Problem:  Divisible Array - https://codeforces.com/contest/1828/problem/A

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
    arr = []
    if n % 2 == 1:
        arr = [i for i in range(1,n+1)]
    
    else:
        for i in range(2,n*2 + 1,2):
            arr.append(i)
    
    print(*arr)
    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()