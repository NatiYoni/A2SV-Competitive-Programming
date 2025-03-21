# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

import sys, collections, math

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve():

    n = inp()
    s = insr()

    
    c = collections.Counter(s)
    min_ = float("inf")
    

    for letter in c:
        left, right = 0, n - 1
        flag = True
        count = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            elif s[right] == letter:
                right -= 1
                count += 1
            
            elif s[left] == letter:
                left += 1
                count += 1
            
            else:
                flag = False
                break

        if flag:
            min_ = min(count, min_)
                
    if min_ != float("inf"):
        print(min_)
    else:
        print(-1)


    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()