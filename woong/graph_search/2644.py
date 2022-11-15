from collections import deque
import sys

input = sys.stdin.readline

# start, target 까지 이동하는데 얼마나 걸리는지를 묻는 문제
def bfs(start, target):
    que = deque()
    que.append((start, 0))
    visited[start] = True

    while que:
        curr, cnt = que.popleft()

        if curr == target:
            return cnt

        for person in relations[curr]:
            if not visited[person]:
                visited[person] = True
                que.append((person, cnt + 1))

    return -1


if __name__ == "__main__":
    people = int(input())
    target1, target2 = map(int, input().split())
    relation_cnt = int(input())
    # [] * (people + 1) 빈 배열에 * 해줘도 하나만 생김
    relations = [[] for _ in range(people + 1)]
    visited = [False] * (people + 1)

    for _ in range(relation_cnt):
        a, b = map(int, input().split())
        relations[a].append(b)
        relations[b].append(a)

    print(bfs(target1, target2))
