# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

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
    s = insr()
    t = insr()
    p = insr()

    p = collections.Counter(p)
    # print(p)
    right = left = 0
    while left < len(s) and right < len(t):
            
            if s[left] == t[right]:
                left += 1
                right += 1
            elif t[right] in p and p[t[right]] > 0:
            
                p[t[right]] -= 1
                right += 1
                
            else:
                print("NO")
                return
    
    
    if left < len(s):
        print("NO") 
        return
    
   
    while right < len(t):
        if t[right] in p and p[t[right]] > 0:
            # print(p)
            p[t[right]] -= 1
            right += 1
            
        else:
            print("NO")
            return

    print("YES")



    pass

def main():
    multi = True # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()