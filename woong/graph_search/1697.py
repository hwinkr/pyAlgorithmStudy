from collections import deque
import sys

# TODO : 동생을 찾기까지 걸리는 시간의 최소 구하기
# ! 이 문제에서는 이동할 수 있는 좌표에 대한 조건이 가장 중요함 0 <= x <= 100000

input = sys.stdin.readline


def bfs(x):
    que = deque()
    que.append(x)

    while que:
        current_x = que.popleft()
        if current_x == target_location:
            print(times[target_location])
            break

        for new_x in (current_x - 1, current_x + 1, current_x * 2):
            # * new_x 가 이동할 수 있는 좌표의 조건을 만족하고, 방문하지 않은 위치인 경우 que에 추가하고 걸리는 시간을 기록한다.
            if 0 <= new_x <= max and not times[new_x]:
                que.append(new_x)
                # * 모든 이동에는 1초가 걸린다. 따라서 이전 위치까지 이동하는데 걸렸던 시간에 +1 을 해준다
                times[new_x] = times[current_x] + 1


current_location, target_location = map(int, input().split())
max = 10**5
# ! 방문 처리와, 이동하는데 걸리는 시간을 times 배열 하나로 해결할 수 있다
# ! 방문하지 않은 좌표라면 0 이 기록되어 있을 것이다. 이 좌표가 x 라면 visited[x] = Fasle 와 같고, x 를 방문하기 전의 좌표까지 이동하는데 걸렸던 시간이 4라면 times[x] = 5 가 되고 times[x] = 0 이 아니기 때문에 방문 처리가 함께 된것과 마찬가지이다.
# * 이 문제에서 얻을수 있는 것은 방문 처리와 문제에서 원하는 값을 저장해두는 것을 하나의 자료구조에서 해결할 수 있는 방법을 알게 된 것
times = [0] * (max + 1)

bfs(current_location)
