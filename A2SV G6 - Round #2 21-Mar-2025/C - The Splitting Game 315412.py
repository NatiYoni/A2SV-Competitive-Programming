# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

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

    n = inp()
    s = insr()

    c = collections.Counter(s)
    pre = [0] * (n )
    post = [0] * (n )

    seen = set()
    

    for i in range(n):
        if s[i] not in seen:
            seen.add(s[i])
        
        pre[i ] = len(seen)
    

    seen.clear()
    for i in range(n-1,-1,-1):
        if s[i] not in seen:
            seen.add(s[i])
        
        post[i ] = len(seen)
 
    
    max_ = 0
    
    for i in range(n - 1):
        max_ = max(max_, pre[i] + post[i + 1])
        i += 1
    
    
    print(max_)
    pass

def main():
    multi = True 
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()