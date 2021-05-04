import math

def function():
    number_of_testcases = int(input())
    res= []
    while (number_of_testcases):
        line = input()
        a = int(math.sqrt(len(line)))
        schema = [''  for  i in range(a**2)]
        for i in range(a**2):
            schema[i] = line[i]
        final_str = ''
        for j in range(a):
            for i in range(a):
                final_str += schema[(a - j-1) + i * (a)]
        res.append(final_str)
        number_of_testcases -= 1
    return res
print(*function(), sep='\n')
        