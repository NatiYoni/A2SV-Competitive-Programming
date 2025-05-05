# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
    n, m = invr()

    parent = [i for i in range(n)]
    metha = [[1,0] for i in range(n)] 
    # neigh_hood = collections.defaultdict(list)

    def find(x):
        ans = 0
        while parent[x] != x:
            x = parent[x]
            ans += metha[x][1]

        return parent[x],ans

    
    def union(x,y):
        x_ = find(x)[0]
        y_ = find(y)[0]

        if x_ != y_:
            if metha[x_] < metha[y_]:
                parent[x_] = y_
                # metha[y_] += metha[x_]
                # neigh_hood[y_].append(x_)
                metha[x_][1] -= metha[y_][1]  
                metha[y_][0] += metha[x_][0]
            else:
                parent[y_] = x_
                
                metha[y_][1] -= metha[x_][1]  
                metha[x_][0] += metha[y_][0]

    for _ in range(m):
        s = insr()

        if s[0] == "add":
            x_,ans = find(int(s[1]) - 1)
            metha[x_][1] += int(s[2])
            

        elif s[0] == "join":
            union(int(s[1]) - 1,int(s[2]) - 1)
            
        else:
            x_,ans = find(int(s[1]) - 1)
            
            print(ans + metha[int(s[1]) - 1][1])
           
    # print(metha)
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()