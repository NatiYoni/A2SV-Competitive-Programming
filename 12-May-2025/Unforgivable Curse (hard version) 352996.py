# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

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

    n, k = invr()
    s = insr()
    t = insr()

    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]

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
           
            parent[x_] = y_
            
            size[x_]+= size[y_]

        

    for i in range(len(s)-k):
        union(i,i+k)
        
        if i+k+1 < len(s):
            union(i,i+k+1)
    
    # print(parent)
    s_ = collections.defaultdict(list)
    t_ = collections.defaultdict(list)
    for i in range(n):
        val = find(i)
        s_[val].append(s[i])
        t_[val].append(t[i])

    for key in s_:
        val1 = collections.Counter(s_[key])
        val2 = collections.Counter(t_[key])
        
        if val1 != val2:
            print("NO")
            break
    else:
        print("YES")
        
        

    pass

def main():
    multi = True  
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()