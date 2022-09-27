n, k = map(int, input().split()) #

type = list()

for i in range(n):
    a = int(input())
    type.append(a)

type.sort(reverse = True) # 코인 큰것부터 정렬

count = 0

for coin in type:
    b = k // coin # a는 k를 코인으로 나눈 몫
    count += b
    k = k % coin # k는 코인으로 나눠줘서 계속 나눠질수있게 함

print(count)
