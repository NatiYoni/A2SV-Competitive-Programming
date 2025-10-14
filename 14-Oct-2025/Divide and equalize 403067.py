# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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
    n = inp()
    a = inlt()

    cnt = dd(int)
    for val in a:
        b = get_prime_factors(val)
        for p in b:
            cnt[p] += 1

    for key,val in cnt.items():
        if val % n != 0:
            print("NO")
            return
    
    print("YES")
    pass

def main():
    multi = True # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()