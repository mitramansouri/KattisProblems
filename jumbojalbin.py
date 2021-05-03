def function():
    number_of_testcases = int(input())
    res = 0
    count = 0
    while (number_of_testcases):
        res += int(input())
        count += 1
        number_of_testcases -= 1
        
    return res - count + 1
print(function())