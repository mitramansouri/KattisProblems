def function():
    number_of_testcases = int(input())
    operation = ['+', '-', '*', '//']
    res = []
    final_res = []
    final_dict = {}
    for i in operation:
        for j in operation:
            for k in operation:
                res.append('4 {} 4 {} 4 {} 4'.format(i, j, k))
    for i in res:
        # if type(eval(i)) == int:
        final_dict[i] = eval(i)
    while (number_of_testcases):
        n = int(input())
        if n in list(final_dict.values()):
            final_res.append('{} = {}'.format(list(final_dict.keys())[list(final_dict.values()).index(n)], n))
        elif n not in final_dict.values():
            final_res.append('no solution')
        number_of_testcases -= 1
    for i in range(len(final_res)):
        if '//' in final_res[i]:
            final_res[i] = final_res[i].replace('//' , '/')
    return final_res 

print(*function(), sep='\n')
