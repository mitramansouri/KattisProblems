def lastFactorialDigit():
    n = int(input())
    res = []
    while (n):
        number = int(input())
        if number >= 5:
            res.append(0)
        elif number == 4:
            res.append(4)
        elif number == 3:
            res.append(6)
        elif number == 2:
            res.append(2)
        elif number == 1:
            res.append(1)
        elif number == 0:
            res.append(1)
        n -= 1
    return res
def print_list(lst):
    for i in lst:
        print(i)

print_list(lastFactorialDigit())
        