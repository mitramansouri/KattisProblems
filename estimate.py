def function():
    n = int(input())
    list = []
    while (n):
        list.append(input())
        n -= 1
    return [len(x) for x in list ]
print(*function(), sep='\n')
