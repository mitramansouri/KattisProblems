def function():
    line = input().split()
    ints = [int(item) for item in line]
    if ints[1] - 45 > 0:
        return [ints[0], ints[1] - 45]
    else:
        if ints[0] == 0:
            return [23, 15 + ints[1]]
        else:
            return [ints[0] - 1, 15 + ints[1]]
print(*function())