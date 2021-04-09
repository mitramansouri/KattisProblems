def oddities():
    n = int(input())
    lst = []
    res = []
    while (n):
        lst.append(int(input()))
        n -= 1
    for item in lst:
        if item % 2 == 0:
            res.append(str(item) + " is even")
        else:
            res.append(str(item) + " is odd")
    return res

def print_list(lst):
    for item in lst:
        print(item)
print_list(oddities())
