import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input())

k = K
stack = list()

#! 아래 주석은 내 코드 시간초과가 난다 왜??
# for i in num:

#     if not stack: # 처음에 스택에 아무것도 없을 때 실행
#         stack.append(i)
#         continue
    
#     for j in reversed(stack): # 넣을 수 보다 앞에 작은수가 있으면 빼는것이 핵심
#         if j < i and k > 0: # 스택안에 넣을 수 보다 작은 것이 있고 빼는 횟수를 초과하지 않았을 때
#             k -= 1
#             stack.pop()

#     stack.append(i)

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])
    
        
print(''.join(stack[:N-K]))