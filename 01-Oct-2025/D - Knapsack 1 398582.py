# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

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
    n, w = invr()
    arr = []
    for _ in range(n):
        a,b   = invr()
        arr.append((b,a))
    
    dp = [[0] * (w + 1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,w+1):
            if j >= arr[i-1][1]: 
                dp[i][j] = max(dp[i-1][j],arr[i-1][0] +  dp[i-1][j-arr[i-1][1]])
            else:
                dp[i][j] = dp[i-1][j]
            
    print(dp[-1][-1])
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()