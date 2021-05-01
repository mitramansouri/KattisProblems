def function():
    n = input()
    line = input().split()
    for i in range(len(line)):
        line[i] = int(line[i])
    return line.index(min(line))
print(function())