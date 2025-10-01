# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

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
    sm = 0
    for _ in range(n):
        a,b   = invr()
        arr.append((b,a))
        sm += b 
        
    dp = [math.inf] * (sm + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(sm, -1,-1):
            dp[j] = min(dp[j],dp[j-arr[i][0]] + arr[i][1])
            
    
    for i in range(sm, -1, -1):
        if dp[i] <= w:
            print(i)
            return 


    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()