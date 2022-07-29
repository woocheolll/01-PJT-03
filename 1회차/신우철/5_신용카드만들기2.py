from os import remove
import sys

sys.stdin = open("_신용카드만들기2.txt")
T = int(input())
for test in range(1, T+1):
    a = input()
    a = a.replace('-','')
    
    if len(a) != 16 : # a 가 16자리가 아닐 때 0
        print(f'#{test} 0')
    
    elif int(a[0:1]) == 3 or int(a[0:1]) == 4 or int(a[0:1]) == 5 or int(a[0:1]) == 6 or int(a[0:1]) == 9: 
        print(f'#{test} 1') # 앞자리가 3,4,5,6,9 이면 1 
    else : 
        print(f'#{test} 0')# 나머지는 0