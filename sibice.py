import math
def sibice():
    line_of_input = input()
    n = int(line_of_input.split()[0])
    tool = int(line_of_input.split()[1])
    arz = int(line_of_input.split()[2])
    maxim = math.floor(math.sqrt(arz ** 2 + tool ** 2))
    res = []
    while (n):
        x = int(input())
        res.append(x)
        n -= 1
    final_res =[]
    for i in res:
        if i <= maxim:
            final_res.append(i)
    for j in res:
        if j in final_res:
            print("DA")
        else:
            print("NE")
sibice()
            
    