def function():
    number_of_testcases = int(input())
    final_res = []
    while (number_of_testcases):
        # each test case 
        trips = int(input())
        res = []
        while (trips):
            location = input()
            if location not in res:
                res.append(location)
            trips -= 1
        final_res.append(len(res))
        number_of_testcases -= 1
    return final_res
print(*function(), sep='\n')
                
            