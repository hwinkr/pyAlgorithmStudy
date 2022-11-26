import sys

input = sys.stdin.readline

# * 설정할 수 있는 높이의 최대

if __name__ == "__main__":
    tree_cnt, target_length = map(int, input().split())
    lengths = list(map(int, input().split()))
    lengths.sort()

    start = 0
    end = lengths[-1]
    setting_length = -1

    while start <= end:
        mid = (start + end) // 2
        tmp_length = 0

        for length in lengths:
            if length - mid > 0:
                tmp_length += length - mid

        if tmp_length >= target_length:
            start = mid + 1
            setting_length = mid
        else:
            end = mid - 1

    print(setting_length)
