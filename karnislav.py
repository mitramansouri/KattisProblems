def function():
    line = input().split()
    for i in range(len(line)):
        line[i] = int(line[i])
    line.sort()
    return int(line[0]) * int(line[2])
print(function())