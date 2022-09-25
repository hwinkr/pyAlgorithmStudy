n, k = map(int, input().split())
li = list()

for i in range(n):
    a = int(input())
    li.append(a)

li.sort(reverse=True) # 크기가 큰 동전순으로 정렬
                      # 거스름돈을 줄 때 크기가 큰 동전부터 세는방법이 깔끔?
count = 0

for coin in li:
    share = k // coin # 거스를 동전의 개수 share
    count = count + share
    k = k % coin # 거스를 동전으로 나눈 나머지

print(count)