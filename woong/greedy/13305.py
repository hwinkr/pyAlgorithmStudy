# 그냥 이동하다가 더 싼 주유소 있으면 들려서 그 주유소 가격으로 변경하면 됩니다
# 마지막 도시의 주유소에 대해서는 생각할 필요가 없음
# 도시의 수 n
# 도로의 수 n - 1

import sys
input = sys.stdin.readline
n = int(input())

road_lst = list(map(int, input().split()))
oil_lst = list(map(int, input().split()))

total = 0
current = oil_lst[0]
total += road_lst[0] * current

for i in range(1, len(road_lst)):
    if oil_lst[i] >= current:
        total += road_lst[i] * current
        continue
    current = oil_lst[i]
    total += road_lst[i] * current


print(total)
