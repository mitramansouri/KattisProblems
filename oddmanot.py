def function():
    n = int(input())
    res = []
    while (n):
        g = int(input())
        numbers = input().split()
        for i in numbers :
            if numbers.count(i) == 1:
                res.append(i)
        n -= 1
    return res
def print_list(lst):
    for i in range(len(lst)):
        print('Case #{}: {}'.format(i + 1, lst[i]))
print_list(function())