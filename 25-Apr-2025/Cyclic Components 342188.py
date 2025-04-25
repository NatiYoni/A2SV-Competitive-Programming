# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

import sys, collections, math, random, bisect

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():
    n,m = invr()

    graph = dd(list)
    for i in range(m):
        a,b = invr()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    
    visited = [0 for _ in range(n)]

    # print(graph)
    @bootstrap
    def dfs(node):
        visited[node] = 1
        # print(node,visited)
        flag = True
        for neigh in graph[node]:
            if  visited[neigh] == 0:
                temp = yield dfs(neigh)
                flag = temp and flag
            
            
        yield (len(graph[node]) == 2 and flag)
    
    ans = 0
    for i in range(n):
        if len(graph[i]) == 2 and visited[i] == 0:

            if dfs(i):
                ans += 1


    print(ans)

    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()