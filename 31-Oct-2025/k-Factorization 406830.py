# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

import sys, collections, math, random, bisect,heapq
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from bisect import bisect_left, bisect_right
from math import gcd, lcm,sqrt,pow, ceil, floor

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
DEBUG = True
# DEBUG = False
def debug(*args):
    if DEBUG:
        import sys
        sys.stderr.write(' '.join(map(str, args)) + "\n")

def get_divisors(num):
    divisors_list = []
    for divisor in range(1, int(num ** 0.5) + 1):
        if num % divisor == 0:
            # divisors_list.append(divisor)
            if divisor != num // divisor:
                if divisor != 1:
                    divisors_list.append((divisor,num // divisor))
                else:
                    divisors_list.append((1,num))
            
    return sorted(divisors_list)

# ===== Number Theory Template =====

# ---- Prime Factorization ----
def get_prime_factors(num):
    factor = 2
    factors_list = []
    n = num
    while factor * factor <= n:
        while n % factor == 0:
            factors_list.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors_list.append(n)
    return factors_list



def solve():
    n , k = invr()
    a = get_divisors(n)
    debug(a)
    
    
    ans = []
    cnt1 = []
    cnt2 = []
    for b,c in a:
        cnt1 = get_prime_factors(b)
        cnt2 = get_prime_factors(c)

        if len(cnt1) + len(cnt2) == k:
            print(*cnt1 + cnt2)
            return
        if  len(cnt1) + len(cnt2) > k:
            diff = len(cnt1) + len(cnt2) - k

            
            while diff > 0:
                if len(cnt1) > 1:
                    cur = cnt1.pop() * cnt1.pop()
                    cnt1.append(cur)
                    # if diff == 1 or len(cnt1) == 0:
                    #     cnt.
                elif len(cnt2) > 1:
                    cur = cnt2.pop() * cnt2.pop()
                    cnt2.append(cur)
                
                diff -= 1

            print(*(cnt1 + cnt2))
            return


    
    print(-1)
        
    pass

t = 1
# t = inp() 
for _ in range(t):
   solve()