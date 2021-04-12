def janice():
    cost = float(input())
    n = int(input())
    res = []
    while (n):
        line_of_input = input()
        res.append(float(line_of_input.split()[0]) * float(line_of_input.split()[1]))
        n -= 1
    return format((sum(res) * cost),'.7f')
print(janice())