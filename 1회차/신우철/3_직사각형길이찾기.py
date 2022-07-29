import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for test in range(1, T+1):
    square1,square2,square3 = map(int,input().split())
    if square1 == square2 and square1 == square3:
        print(f'#{test} {square1}')
    elif square1 == square2 and square1 != square3:
        print(f'#{test} {square3}')
    elif square1 != square2 and square2 != square3:
        print(f'#{test} {square2}')
    elif square1 != square2 and square1 != square3:
        print(f'#{test} {square1}')