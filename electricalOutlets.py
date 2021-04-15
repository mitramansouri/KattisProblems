def function():
    n = int(input())
    outlets = []
    while (n):
        line_of_input = input().split()
        for i in range(len(line_of_input)):
            line_of_input[i] = int(line_of_input[i])
        outlets.append(sum(line_of_input[1:]) - line_of_input[0]+1)
        n -= 1
    return outlets
print(*function(), sep="\n")
        