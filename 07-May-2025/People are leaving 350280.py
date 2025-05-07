# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys, collections, math, random, bisect

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input().split(" "))
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():

    n,q = invr()
    parent = [i for i in range(n)]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]] 
            x = parent[x]
        return x
    

    for _ in range(q):
        s = insr()
        num = int(s[1])
        if s[0] =="?":
            x = find(num -1)
            print(x + 1) if x != -1 else print(-1)
        else:
            if num != n:
                parent[num - 1] = num
            else:
                parent[num - 1] = -1
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()