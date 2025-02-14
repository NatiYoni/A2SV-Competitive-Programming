# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n,k = map(int,input().strip().split())
nums = list(map(int,input().strip().split()))

count_num = defaultdict(int)
maxm = 0
res = []
left = 0
for i in range(n):
    
    count_num[nums[i]] += 1
    while len(count_num) > k and left < n:
        count_num[nums[left]] -= 1
        if count_num[nums[left]] == 0:
            del count_num[nums[left]]
        left += 1
    if maxm < (i - left + 1):
        maxm = (i-left + 1)
        res = [left+1,i+1]
    

print(*res)