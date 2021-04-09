def pet():
    n = 5
    lst = []
    res = []
    while (n):
        line_of_input = input()
        lst = line_of_input.split()
        i = 0
        for item in lst:
            lst[i]= int(item)
            i+=1
        res.append(sum(lst))
        n -= 1
    maxim = max(res)
    
    for i in range(len(res)):
        if res[i] == maxim:
            return str(i + 1) + " " + str(maxim)


print(pet())
