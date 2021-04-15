def cake():
    w = int(input())
    n = int(input())
    s = 0
    while (n):
        line_of_input = input()
        wi = int(line_of_input.split()[0])
        li = int(line_of_input.split()[1])
        s += li * wi
        n -= 1
    return s // w 
print(cake())
        

