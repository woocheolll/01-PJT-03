import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for test in range(1, T+1):
    a = input()[::-1]
    # 거꾸로 뒤집기
    if a in ['b','d','p','q']:
        mirror = a.replace('b','d') 



    print(f'#{test} {mirror}')
        
    
    
    
    
            
    
    
    
    
    
