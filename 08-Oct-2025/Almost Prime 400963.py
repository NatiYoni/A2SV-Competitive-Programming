# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

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

    p_d = [[] for _ in range(n+1)] 
    valid = [True]  * (n+1)
    i = 2
    while i <= n:
        if valid[i]:
            cnt = 2

            while cnt * i <= n:
                p_d[i*cnt].append(i)
                valid[i*cnt] = False
                cnt += 1
        i += 1

    ans = 0
    for arr in p_d:
        if len(arr) == 2:
            ans += 1

    print(ans)


    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()