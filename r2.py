def r2():
    line_of_input = input()
    lst = line_of_input.split()
    r1 = int(lst[0])
    s = int(lst[1])
    r2 = 2 * s - r1
    return r2
    
print(r2())
