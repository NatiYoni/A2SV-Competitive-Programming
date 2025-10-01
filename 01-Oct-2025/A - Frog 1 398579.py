# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

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
    arr = inlt()
    dp = [math.inf] * (n+1)
    dp[1] = 0
    dp[2] = abs(arr[1] - arr[0])

    for i in range(3,n + 1):
        dp[i] = min((dp[i-1] + abs(arr[i-1] - arr[i-2]), (dp[i-2] + abs(arr[i-1] - arr[i-3])))) 
    
    # print(dp)
    print(dp[-1])

    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()