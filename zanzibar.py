def function():
    n = int(input())
    final_res = []
    res = 0
    while (n):
        test_case = input().split()
        for i in range(1,len(test_case)):
            if int(test_case[i]) > 2 * int(test_case[i - 1]):
                res += int(test_case[i]) - int(test_case[i - 1])*2
        final_res.append(res)
        res = 0
        n -= 1
    return final_res
print(*function(), sep='\n')
            
        