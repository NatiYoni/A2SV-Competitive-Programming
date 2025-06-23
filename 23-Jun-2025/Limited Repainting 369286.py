# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

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
    n,k = invr()
    s = insr()
    arr = inlt()

    low = 0
    high = max(arr)
    f = [0]
    length = [len(s)]
    while f[0] < length[0] and s[f[0]] == "R":
        f[0] += 1
    
    

    def checker(mid,k):
        mx = 0
        flag = False
        for i in range(f[0],length[0]):
            if s[i] == "B" and arr[i] > mid:
                if not flag :
                    if k <= 0:
                        mx = max(mx,arr[i])
                    else:
                        k -= 1
                        flag = True
            else:
                if flag:
                    if arr[i] > mid:
                        flag = False
                    
        
            
        return mx <= mid
            
                

        pass

    ans = 0
    while low <= high:
        mid = low + (high - low)//2

        if checker(mid,k):
            high = mid - 1
            ans = mid
        
        else:
            low = mid + 1
    
    print(ans)


    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()