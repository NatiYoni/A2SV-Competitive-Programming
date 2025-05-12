# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

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
    n, m, k = invr()
    arr = inlt()
    gov = set(arr[i] - 1 for i in range(k))

    parent = [i for i in range(n)]
    size = [1 for i in range(n)]

    # ans = [0 for _ in range(n)]
    def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

    def union(x, y):
        x_ = find(x)
        y_ = find(y)

        if x_ != y_:
            if size[x_] < size[y_]:
                x_, y_ = y_, x_
            parent[y_] = x_
            size[x_]+= size[y_]
            

    ans = 0
    for _ in range(m):
        x,y = invr()
        union(x-1,y-1)

    gov_roots = set(find(g) for g in gov)
    max_city = -1
    root = -1
   
    for val in gov_roots:
        if size[val] > max_city:
            max_city = size[val]
            root = val
    # print(root)
    for i in range(n):
        val = find(i)
        if val not in gov_roots:
            union(i,root)

    res = set()
    for i in range(n):
        res.add(find(i))
    
    ans = 0
    for val in res:
        temp = size[val]
        ans += (temp * (temp - 1))//2
    
    print(ans-m)


    
def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()