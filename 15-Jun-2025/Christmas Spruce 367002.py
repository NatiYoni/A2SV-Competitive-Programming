# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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
    graph = dd(list)


    for i in range(2,n+1):
        graph[inp()].append(i)

    
    for key,val in graph.items():
        ans = 0
        if len(val) < 3:
            print("No")
            return

        for neigh in val:
            if neigh not in graph:
                ans += 1
        
        if ans < 3:
            print("No")
            return 

        
    
    print("Yes")


    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()