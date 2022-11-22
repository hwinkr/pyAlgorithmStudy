import sys

input = sys.stdin.readline

n, k = map(int, input().split())
delete_count = k
# * 파이썬 문자열도 Js 처럼 유사 배열 객체인듯
nums_list = str(input())

stack = []

# * 현재 스택에서 가장 위에 있는 값을 가능한 크게 만든다.

for i in range(len(nums_list)):
    while stack and k > 0:
        if stack[-1] < nums_list[i]:
            k -= 1
            stack.pop()
        else:
            break
    stack.append(nums_list[i])

print("".join(stack[: n - delete_count]))
