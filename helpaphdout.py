def function():
    number_of_testcases = int(input())
    res = []
    while (number_of_testcases):
        line = input()
        if line == 'P=NP':
            res.append('skipped')
        else:
            numbers = line.split('+')
            res.append(int(numbers[0]) + int(numbers[1]))
        number_of_testcases -= 1
    return res
print(*function() , sep='\n')