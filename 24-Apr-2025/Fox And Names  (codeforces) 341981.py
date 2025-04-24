# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

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

    s = []
    for i in range(n):
        temp = input()
        s.append(temp)
    
    graph = dd(list)
    degree = [0 for _ in range(26)]

    for i in range(1,len(s)):      
        
        l = 0
        while  len(s[i-1]) > l < len(s[i]) and  s[i-1][l] == s[i][l]:
            l += 1

        if (len(s[i-1]) == l  or l == len(s[i])) and len(s[i]) < len(s[i-1]):
            print("Impossible")
            return

        if len(s[i-1]) > l < len(s[i]):

            ch1 = ord(s[i - 1][l])  - 97
            ch2 = ord(s[i][l])  - 97

            graph[ch1].append(ch2)
            degree[ch2] += 1

        
        
    # print(graph)
    # print(degree)


    dq = collections.deque()
    for i,val in enumerate(degree):
        if val == 0:
            dq.append(i)
    # print(dq)
    ans = []
    while dq:
        for _ in range(len(dq)):
            node = dq.popleft()

            ch = chr(node + 97 )
            ans.append(chr(node + 97 ))

            for neigh in graph[node]:
                degree[neigh] -= 1

                if degree[neigh] == 0:
                    dq.append(neigh)
                    
    # print(ans,len(ans))
    # print(degree)

    if len(ans) != 26:
        print("Impossible")
    else:
        print("".join(ans))

    

    




















    # seen = set()
    # pre = s[0]
    # res = []

    # for l in s:
    #     if pre != l and l in seen:
    #         print("Impossible") 
    #         return
        
    #     if (l not in seen) or (l == pre):
    #         if l not in seen:
    #             res.append(l)
    #         pre = l
    #         seen.add(l)
        
    # print(res)
    # ans = []
    # # print(chr(96))
    # for i in range(26):
    #     if chr(97 + i) not in seen:
    #         ans.append(chr(97 + i))
        
    #     elif chr(97 + i) == res[0]:
    #         ans.extend(res)
        

    

    
    # print("".join(ans))

    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()