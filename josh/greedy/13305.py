n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

now = price[0]
result = road[0]*price[0]

for i in range(1, len(road)):
    if price[i] <= now:
        now = price[i]
        result = result + road[i] * now

    else: result = result + road[i] * now

print(result)