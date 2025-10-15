# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

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

    n = inp()
    a = inlt()
    # fact = collections.Counter(get_prime_factors(a[0]))
    # for i,val in enumerate(a,start=1):
    #     cnt = collections.Counter(get_prime_factors(val))

    #     for val in cnt:
    #         if val != 2 and val != 3:
    #             if fact[val] != cnt[val]:
    #                 print("NO")
    #                 return
    # print("YES")

    na = dd(int)
    for val in a:
        while val % 2 == 0:
            val //=  2
        while val % 3 == 0:
            val //= 3

        na[val] += 1
    
    
    print("YES" if len(na) == 1 else "NO")


    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()