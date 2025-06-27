# Problem: Where's the Bishop? - https://codeforces.com/problemset/problem/1692/C

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

directions = [(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():
    
    s = [insr() for _ in range(8)]
    # print(s)
    for i in range(8):
        for j in range(8):
            if s[i][j] == "#":
                
                cnt = 0
                for dx,dy in directions:
                    
                    nr = i + dx
                    nc = j + dy

                    if is_in_bounds(s,nr,nc):
                        if s[nr][nc] == "#":
                            cnt += 1

                if cnt == 4:
                    print(i+1,j+1)
                        
    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        insr()
        solve()

if __name__ == '__main__':
    main()