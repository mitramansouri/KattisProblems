def function():
    n = int(input())
    final_res = []
    while (n):
        res = 0
        stores = int(input())
        line = input().split()
        for i in range(len(line)):
            line[i] = int(line[i])
        line.sort()
        middle = (line[-1] - line[0]) / 2
        for i in range(len(line)-1):
            res += line[i + 1] - line[i]
        res += line[-1] - middle
        res += middle - line[0]
        final_res.append(int(res))
        n-= 1
        
    return final_res
print(*function())
    