import sys

sys.stdin = open("_최빈수구하기.txt")
T = int(input())
for test in range(1, T+1):
    a = list(map(int,input().split()))
    for i in a:
        for j in range(0,101):
            j = int(j)
            i = int(i)
            count_ = i.count(j)

        print(count_)