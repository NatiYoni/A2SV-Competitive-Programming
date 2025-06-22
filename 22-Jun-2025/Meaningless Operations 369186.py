# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

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
    length = n.bit_length()
    bit = ["0"] * length
    
    l = 0
    while l < length:
        if not n & (1 << l):
            bit[l] = "1"
        l += 1
    num = int("".join(reversed(bit)),2)
    if num:
        print(max(num ^ n,num & n))
    else:
        
        res = 1
        for b in range(2, int(math.sqrt(n)) + 1):
            if n % b == 0:
                res = max(res, b, n // b)
        
        print(res)
    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()