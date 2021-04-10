def nastyhacks():
    n = int(input())
    lst =[]
    while (n):
        line_of_input = input()
        r = int(line_of_input.split()[0])
        e = int(line_of_input.split()[1])
        c = int(line_of_input.split()[2])
        lst.append((e - r) - c)
        n -= 1
    for i in lst:
        if i < 0:
            print("do not advertise")
        elif i == 0:
            print("does not matter")
        elif i > 0:
            print("advertise")
nastyhacks()
