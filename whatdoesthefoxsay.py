def function():
    number_of_testcases = int(input())
    animals = []
    res = []
    while (number_of_testcases):
        records = input().split()
        line = input()
        while (line != 'what does the fox say?'):
            line = line.split()
            animals.append(line[2])
            line = input()
        for i in animals:
            records = list(filter((i).__ne__, records))
        res.append(' '.join(records))
        number_of_testcases -= 1
    return res
print(*function(), sep='\n')
