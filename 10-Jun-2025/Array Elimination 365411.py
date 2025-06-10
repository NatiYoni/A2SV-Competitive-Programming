# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

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
    

    cnt = [0] * 30
    for val in arr:
       for i in range(30):
            if (val >> i) & 1:  
                cnt[i] += 1
    
    ans = []
    for k in range(1,n+1):
        flag = True
        for val in cnt:
            if val % k != 0:
                flag = False

        
        if flag:
            ans.append(k)
       
           
    print(*ans)

    pass

def main():
    multi = True
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()