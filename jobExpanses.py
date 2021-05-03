def function():
    number_of_testcases = int(input())
    line = input().split()
    res = 0 
    for i in line:
        if int(i) < 0:
            res += int(i)
    return abs(res)
print(function())