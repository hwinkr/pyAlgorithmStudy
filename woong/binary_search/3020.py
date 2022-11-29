# 개똥벌레
# 이 문제는 누적합으로도 풀 수 있다고 한다,, 하지만 누적합을 잘 모른다

# * 모든 높이를 다 가봐야한다, 그래서 높이 방문은 이분 탐색이 아니다
# * 핵심은 개똥벌레가 제일 처음 벽을 부수는 높이의 인덱스를 찾는 것이다.
# * 벽이 5개가 있고 개똥벌레가 인덱스 1의 벽부터 부수기 시작한다면 나머지 인덱스 2, 3, 4 의 벽은 무조건 부술 수 밖에 없다
# * 따라서 인덱스가 1이면 부수는 벽의 갯수는 5 - 1 = 4 이다.
# * 벽의 높이들이 오름차순 정렬 되어 있다고 가정하고, 이 인덱스를 이분탐색을 통해서 찾아 시간 복잡도를 줄여야 한다.

import sys

input = sys.stdin.readline


def bi_search(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if target < arr[mid]:
            # 인덱스의 최솟값을 찾는다
            end = mid - 1
            # ans = mid
        else:
            start = mid + 1

    return start


width, height = map(int, input().split())
blocks_down = []
blocks_up = []

for i in range(width):
    if i % 2 == 0:
        blocks_down.append(int(input()))
    else:
        blocks_up.append(int(input()))

blocks_down.sort()
blocks_up.sort()

destory_cnt = width
path_cnt = 0

for i in range(height):
    down_idx = bi_search(blocks_down, i + 0.5, 0, len(blocks_down) - 1)
    up_idx = bi_search(blocks_up, height - i - 0.5, 0, len(blocks_up) - 1)

    down_cnt = len(blocks_down) - down_idx
    up_cnt = len(blocks_up) - up_idx

    if down_cnt + up_cnt < destory_cnt:
        destory_cnt = down_cnt + up_cnt
        path_cnt = 1
    elif down_cnt + up_cnt == destory_cnt:
        path_cnt += 1

print(destory_cnt, path_cnt)
