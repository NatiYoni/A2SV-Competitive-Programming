# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import sys, collections, math

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():

    n, m , a  = invr()

    row = (n + a - 1) // a
    col = (m + a - 1) // a

    # Total number of flagstones
    ans = row * col
    print(ans)

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()