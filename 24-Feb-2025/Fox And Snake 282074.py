# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A


def invr():
    return map(int, input().split())



def solve():
    n, m = invr()
    for i in range(1,n + 1):
        if i % 2 == 1:
            print('#' * m)
        else:
            if i % 4 == 0:
                print("#" + "." * (m-1))
            else:
                print("." * (m-1) + "#")


def main():
    multi = False 
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()