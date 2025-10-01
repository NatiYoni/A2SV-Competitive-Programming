# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

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
    arr = [inlt() for _ in range(n)]
    dp = [[0,0,0] for _ in range(n+1)]
    
    for i in range(1,n+1):
        dp[i][0] =  arr[i-1][0] + max(dp[i-1][1],dp[i-1][2])    
        dp[i][1] = arr[i-1][1] + max(dp[i-1][0],dp[i-1][2])
        dp[i][2] = arr[i-1][2] + max(dp[i-1][0],dp[i-1][1])
    
    # print(dp)
    print(max(dp[-1]))

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()