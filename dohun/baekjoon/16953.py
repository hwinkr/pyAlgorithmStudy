if __name__ == "__main__":
    a, b = map(int, input().split())
    
    count = 1
    while a < b:
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            b = -1
        count += 1

    print(count if a == b else -1)