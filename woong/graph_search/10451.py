import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
test_cnt = int(input())


def dfs(x):
    visited[x] = True
    if not visited[nums[x]]:
        dfs(nums[x])


for _ in range(test_cnt):
    nums_size = int(input())
    visited = [False] * (nums_size + 1)
    # * 처음 알게된 문법이다.
    # * nums = [0] * 5 해주면 [0, 0, 0, 0, 0] 배열이 생성된다
    # * nums = [1] + [0] * 4 해주면 [1, 0, 0, 0, 0] 배열이 생성된다.
    # ! 문제에서는 입력값이 1 ~ nums_size 이기 때문에 인덱스 0 을 전혀 사용하지 않는다. 따라서 인덱스 0의 값을 따로 정해줘야한다.
    nums = [0] + list(map(int, input().split()))
    permutaion_cnt = 0

    for i in range(1, nums_size + 1):
        if not visited[i]:
            dfs(i)
            permutaion_cnt += 1

    print(permutaion_cnt)
