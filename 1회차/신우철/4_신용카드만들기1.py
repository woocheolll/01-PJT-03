import sys

sys.stdin = open("_신용카드만들기1.txt")
T = int(input())
for test in range(1, T+1):
    a = list(map(int,input().split()))
    b = sum(a[0:1])+sum(a[2:3])+sum(a[4:5])+sum(a[6:7])+sum(a[8:9])+sum(a[10:11])+sum(a[12:13])+sum(a[14:15])
    # 홀수자리 더하기
    c = sum(a[1:2])+sum(a[3:4])+sum(a[5:6])+sum(a[7:8])+sum(a[9:10])+sum(a[11:12])+sum(a[13:14])
    # 짝수자리 더하기
    d = b * 2
    # 홀수자리 *2
    e = c + d
    # 짝수자리 홀수자리 더하기
    N = e % 10
    # 나머지 구하기
    
    
    if N == 0 : # N이 0일때는 그대로 출력
        print(f'#{test} {N}')
    elif N != 0 :# N이 0이 아닐때는 10 - N 을 출력 
        print(f'#{test} {10-N}')
        

