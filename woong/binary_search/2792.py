# * 질투심의 최솟값
# * 보석을 갖지 못하는 학생이 있어도 된다.
# ! 학생은 같은 색상의 보석만 가질 수 있음, 모든 보석을 사용해야 한다.

import sys

inpyt = sys.stdin.readline

students, jewel_type = map(int, input().split())
colors = [int(input()) for _ in range(jewel_type)]
colors.sort()


start = 1
end = colors[-1]
ans = 0

while start <= end:

    tmp_students = 0
    mid = (start + end) // 2

    for color in colors:
        if color % mid == 0:
            tmp_students += color // mid
        else:
            tmp_students += color // mid + 1

    if tmp_students <= students:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
