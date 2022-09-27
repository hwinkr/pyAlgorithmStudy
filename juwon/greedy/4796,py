import math # floor함수를 쓰기위해 - 소수점을 버린다

n = 1
while True: # V일 중 최대한 P일 만큼 가고 나머지 일에대해 L과 비교하여 구하면 된다
    camp = list(map(int, input().split())) 
    
    if camp == [0,0,0]:
        break
                              # '//'연산자를 쓰면 몫을 바로 구할 수 있다고 하네요
    share = camp[2] / camp[1] # V를 최대한 P로 나누고
    share = math.floor(share) # 나머지는 버린 수 share
     
    remainder = camp[2] % camp[1] # V를 P로 나눴을 때 나머지 remainder
 
    if remainder >= camp[0]:
        camping_day = camp[0] * share + camp[0]
    else:
        camping_day = camp[0] * share + remainder

    print(f"Case {n}: {camping_day}")
    
    n = n + 1