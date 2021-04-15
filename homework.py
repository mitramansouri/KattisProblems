def function():
    line_of_input = input().split(';')
    res = 0
    temp = []
    for i in line_of_input:
        if not '-' in i :
            # its a single number 
            res += 1
        else:
            temp = i.split('-')
            res += (int(temp[1]) - int(temp[0]) + 1)
    return res

print(function())