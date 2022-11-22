import sys

input = sys.stdin.readline

# * 길이가 서로 다른 k 개의 랜선으로 길이가 같은 N 개의 랜선 만들기
# ! n개 보다 많이 만드는 것도 n 개를 만드는 것에 포함
# ! 자를 수 있는 랜선의 최대 길이

have_cnt, make_cnt = map(int, input().split())
lines = [int(input()) for _ in range(have_cnt)]
lines.sort()

start = 1  # * 랜선을 못자르는 경우는 없다, start 를 0으로 하면 mid 값이 0 이 되는 경우가 생긴디 => (0 + 1) // 2 = 0
end = lines[-1]
max_length = 0

while start <= end:
    mid = (start + end) // 2

    tmp_cnt = 0

    for i in range(have_cnt):
        # ! mid 값이 0이면 무한대로 발산, 런타임 에러 발생
        tmp_cnt += lines[i] // mid
    # * tmp_cnt 가 make_cnt 보다 크다 => 자른 랜선의 길이가 너무 짧다 길이를 늘려야 한다
    if tmp_cnt >= make_cnt:
        start = mid + 1
        max_length = mid
    else:
        end = mid - 1

print(max_length)
