# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int,input().split())
arr = list(map(int, input().split()))

left = 0
sum_ = 0
max_length = 0


for right in range(n):

    sum_ += arr[right]

    while sum_ > t:
        sum_ -= arr[left]
        left += 1
    max_length = max(max_length, right - left + 1)

print(max_length)