import sys
input = sys.stdin.readline


def solution():
    test = int(input())
    pass_lst = []

    for _ in range(test):
        n = int(input())
        ranks = [0] * (n + 1)
        for _ in range(n):
            s1, s2 = map(int, input().split())
            ranks[s1] = s2

        cnt = 1
        curr = ranks[1]

        for rank in ranks[2:]:
            if rank < curr:
                cnt += 1
                curr = rank
        pass_lst.append(str(cnt))

    print('\n'.join(pass_lst))


if __name__ == "__main__":
    solution()
