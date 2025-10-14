# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

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
    n,m =  invr()
    a = inlt()
    b = inlt()

    mn = a[0]

    a = [val - mn for val in a]
    # print(a)
    gc = 0

    for val in a:
        gc = math.gcd(gc,val)
    
    # print(gc)
    ans = []
    for val in b:
        ans.append(math.gcd(val + mn, gc))
        
    print(*ans)

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()