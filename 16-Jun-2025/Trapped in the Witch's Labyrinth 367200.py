# Problem: Trapped in the Witch's Labyrinth - https://codeforces.com/problemset/problem/2034/C

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

directions = [(-1,0),(0,1),(0,-1),(1,0)]

rand_no = random.randint(1, 1000000000)

def solve():
    n, m = invr()
    
    s = [insr() for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    outs = collections.deque()
    for i in range(n):
        for j in range(m):
            if ((i == 0 and s[i][j] == "U") or (i == n - 1 and s[i][j] == "D") or 
                (j == 0 and s[i][j] == "L") or (j == m-1 and s[i][j] == "R")):
                outs.append((i,j))
    
    while outs:
        row,col = outs.popleft()
        visited[row][col] = 1

        for x,y in directions:
            nr,nc = row + x, col + y

            if is_in_bounds(s,nr,nc) and visited[nr][nc] == 0:
                if x == -1 and s[nr][nc] == "D":
                    outs.append((nr,nc))
                elif x == 1 and s[nr][nc] == "U":
                    outs.append((nr,nc))
                elif y == -1 and s[nr][nc] == "R":
                    outs.append((nr,nc))
                elif y == 1 and s[nr][nc] == "L":
                    outs.append((nr,nc))
    
    
    for i in range(n):
        for j in range(m):
            if s[i][j] == "?":
                count = 0
                bound = 0
                for x,y in directions:
                    nr,nc = i + x, j + y
                    if is_in_bounds(s, nr, nc) :
                        bound += 1

                        if visited[nr][nc] == 1:
                            count += 1
    
                if bound - count == 0:
                    visited[i][j] = 1
                else:
                    visited[i][j] = 0

    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                ans += 1
            

    print(ans)


def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()