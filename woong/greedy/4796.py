import sys
input = sys.stdin.readline

i = 1

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    day = 0
    day += (v // p) * l
    if v % p > l:
        day += l
    else:
        day += v % p

    print(f"Case {i}: {day}")
    i += 1
