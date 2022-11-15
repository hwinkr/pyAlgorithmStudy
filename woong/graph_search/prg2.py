from collections import deque


def solution(numbers, target):
    answer = 0
    idx = 0
    que = deque()
    que.append((-numbers[idx], idx + 1))
    que.append((numbers[idx], idx + 1))

    while que:
        current_number, next_index = que.popleft()

        if next_index == len(numbers):
            if current_number == target:
                answer += 1
            continue

        que.append((current_number + numbers[next_index], next_index + 1))
        que.append((current_number - numbers[next_index], next_index + 1))

    return answer
