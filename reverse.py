def my_reverse():
    n = int(input())
    list = []
    while (n):
        list.append(int(input()))
        n -= 1
    list.reverse()
    return list
print(*my_reverse(), sep='\n')