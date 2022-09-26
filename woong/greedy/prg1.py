def solution(n, lost, reserve):
    answer = 0
    # 모든 학생이 체육복을 하나 가지고 있다고 가정하고 출발.
    # 도난 당했다? -1
    # 여분이 있다? -1
    # 여분이 있지만 도난 당했다? 그냥 1
    cnts = [1] * (n + 1)
    for i in lost:
        cnts[i] -= 1
    for j in reserve:
        cnts[j] += 1

    for i in range(1, n + 1):
        if cnts[i] == 0:
            for x in (i - 1, i + 1):
                if x < 1 or x > n:
                    continue
                if cnts[x] > 1:
                    cnts[x] -= 1
                    cnts[i] += 1
                    break

    for i in range(1, n + 1):
        if cnts[i] > 0:
            answer += 1

    return answer
