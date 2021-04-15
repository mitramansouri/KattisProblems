def function():
    line_of_input = input().split()
    dic = {'1': 1, '2': 1, '3': 2, '4': 2, '5': 2, '6': 8}
    res = []
    for i in range(len(line_of_input)):
        res.append( dic[str(i+1)] - int(line_of_input[i]))
    return res
print(*function())        
