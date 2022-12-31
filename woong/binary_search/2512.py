# 예산
# * 각 지방들에게 분배할 수 있는 예산 상한액의 최댓값
# 시간복잡도는 lms 강의자료 참고
import sys

input = sys.stdin.readline

locals = int(input())
requests = list(map(int, input().split()))
total_money = int(input())

requests.sort()
start = 0
end = requests[-1]

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for money in requests:
        if money < mid:
            tmp += money
        else:
            tmp += mid

    if tmp > total_money:  # 이 경우는, 현재 mid 값이 너무 큼 따라서 줄여야함
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)
