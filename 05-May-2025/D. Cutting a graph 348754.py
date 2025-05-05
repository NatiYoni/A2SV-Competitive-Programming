# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
    n,m,k = invr()

    [invr() for _ in range(m)]

    s = [insr() for _ in range(k)]
    s.reverse()

    metha = [1 for _ in range(n)]  
    parent = [i for i in range(n)]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]] 
            x = parent[x]
        return x

    def union(x, y):
        x_ = find(x)
        y_ = find(y)
        if x_ != y_:
            if metha[x_]< metha[y_]:
                x_, y_ = y_, x_
            parent[y_] = x_
            metha[x_]+= metha[y_]
    ans = []
    for a,b,c in s:
        b = int(b) - 1
        c = int(c) - 1

        if a == "cut":
            union(b,c)
        else:
            if find(b) == find(c):
                ans.append("YES")
            else:
                ans.append("NO")
    
    ans.reverse()

    for a in ans:
        print(a)
    
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()