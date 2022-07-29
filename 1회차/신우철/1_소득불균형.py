import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test in range(1, T+1):
    count_ = 0
    people = int(input())
    #사람의 수 입력
    money = list(map(int,input().split()))
    # 돈 입력
    sum_ = sum(money)
    # 돈을 다 더해서
    avg = sum_ // people
    # 평균 구하기
    for i in money:  
        if i <= avg : # i가 평균보다 작거나 같으면
            count_ += 1 # +1 을 한다
     
    print(f'#{test} {count_}')


    