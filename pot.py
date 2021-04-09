def pot():
    n = int(input())
    res = 0
    while (n):
        item = input()
        key = int(item[:-1])
        power = int(item[-1])
        res += key**power
        n -= 1
    return res

print(pot())
        
