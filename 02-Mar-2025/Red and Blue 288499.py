# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))


def solve():
    n = inp()
    r = inlt()
    m = inp()
    b = inlt()


    
    for i in range(1,n): 
        r[i] += r[i-1]
    for i in range(1,m):
        b[i] += b[i-1] 
        
    num_b , num_r = max(b) , max(r)
    print(max(max(num_b,0) + max(num_r,0),0))        



def main():
    multi = True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()