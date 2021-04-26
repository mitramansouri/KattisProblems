
def function():
    n = int(input())
    line = ''
    while (n):
        line += input()
        n -= 1
    res = 0
    for i in range(1,len(line)):
        if line[i] == line[i - 1]:
            res += 1
    return res

print(function())