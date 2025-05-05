# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
    n,m = invr()

    arr = [inlt() for _ in range(m)]
    arr.sort(key = lambda x: x[2])
    # print(arr)

    metha = [[1,0] for _ in range(n)]  
    parent = [i for i in range(n)]
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]] 
            x = parent[x]
        return x
    
    def union(x, y, c):
        x_ = find(x)
        y_ = find(y)
        if x_ != y_:
            if metha[x_][0] < metha[y_][0]:
                x_, y_ = y_, x_
            parent[y_] = x_
            metha[x_][0] += metha[y_][0]
            metha[x_][1] += metha[y_][1] + c  
    

    for a,b,c in arr:
        union(a - 1,b - 1, c)
        
    
    print(metha[find(0)][1])
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()