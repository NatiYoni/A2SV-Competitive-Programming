# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

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

    x, y = invr()

    if x == y:
        print(-1)
        return 
    
    x_ = x.bit_length()
    y_ = y.bit_length()

    if x > y:
        print(2**x_ - x)
    else:
        print(2**y_ - y)
    # arr1 = [0] * 30
    # arr2 = [0] * 30

    # for i in range(30):
    #     if (1 << i) & x :
    #         arr1[i] = 1
        
    #     if (1 << i) & y :
    #         arr2[i] = 1
    
    # ans = ["0"] * 30
    # for i in range(30):
    #     if arr1[i] == 1 and arr2[i] == 1:
    #         ans[i] = str(1)
        

    
    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()