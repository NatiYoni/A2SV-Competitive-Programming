# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

import sys, collections, math, random, bisect,heapq
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from bisect import bisect_left, bisect_right
from math import gcd, lcm,sqrt,pow, ceil, floor, comb, perm

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())
inword = lambda: list(input().split(' '))
def yn(flag): return 'YES' if flag else 'NO'

def dd(type_func=int):
    return defaultdict(type_func)

def in_bound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand = random.randint(1, 1000000000)

# ---------- DEBUG CONFIG ----------
#DEBUG = True
DEBUG = False
def debug(*args):
    if DEBUG:
        import sys
        sys.stderr.write(' '.join(map(str, args)) + "\n")

def solve():
    n = inp()

    print(comb(n,5) + comb(n,6) + comb(n, 7))
    pass

t = 1
# t = inp() 
for _ in range(t):
   solve()