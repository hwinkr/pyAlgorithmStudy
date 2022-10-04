# import sys
# input = sys.stdin.readline

# t = int(input())

# result_list = list()

# for _ in range(t):
#     li = list()
#     n = int(input())

#     for _ in range(n):
#         grade = list(map(int, input().split()))
#         li.append(grade)
        
#     li.sort(key=lambda x: x[0])
#     x = 1    
#     while True:
#         if x == len(li):
#             break
        
#         if li[x-1][1] < li[x][1]:
#             li.pop(x)
#         else:
#             x = x + 1
            
#     li.sort(key=lambda x: x[1])
#     y = 1    
#     while True:
#         if y == len(li):
#             break
        
#         if li[y-1][0] < li[y][0]:
#             li.pop(y)
#         else:
#             y = y + 1
        
#     print(len(li))

#todo 위의 코드로 했다가 시간초과가 나서 
#todo 구글에서 참고해 아래의 코드로 바꿨습니다

import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수 t

result_list = list()

for _ in range(t):
    li = list()
    n = int(input()) # 지원자 숫자 n

    for _ in range(n): # list에 지원자를 저장후
        grade = list(map(int, input().split()))
        li.append(grade)
    
    li = sorted(li, key=lambda x: x[0]) # 서류심사를 기준으로 정렬한다
    
    print(li)
    

    count = 1 # 합격한 사람 수 
              # 서류심사에 1등한 사람은 무조건 합격하므로 1부터 시작한다
    top = li[0][1] # 서류 심사 1등한 사람을 기준으로 
    for i in range(1, len(li)): 
        if li[i][1] < top: # 만약 면접심사가 더 높은 사람이 나타나면 합격시키고
            top = li[i][1] # 그 사람을 기준으로 다시 합격시킬 사람을 찾는다
            count = count + 1
    
    print(count)