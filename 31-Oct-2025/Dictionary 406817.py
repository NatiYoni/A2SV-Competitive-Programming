# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

import sys, collections, math, random, bisect,heapq

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def in_bound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand = random.randint(1, 1000000000)

def solve():
    n= inp()

    for _ in range(n):
        s = insr()

        ch2 = ord(s[0]) - 97
        ch1 = ord(s[1]) - 97

        if ch1 < ch2:
            ch1 += 1
        print(ch2 * 25 + ch1 )

    pass

t = 1
# t = inp() 
for _ in range(t):
   solve()