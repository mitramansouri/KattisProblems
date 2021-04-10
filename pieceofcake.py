def poc():
    line_of_input = input()
    sides = int(line_of_input.split()[0])
    h = int(line_of_input.split()[1])
    v = int(line_of_input.split()[2])
    if h >= sides / 2:
        if v >= sides / 2:
            valume = h * v * 4
        else:
            valume = (sides - v) * h * 4
    elif h <= sides / 2:
        if v >= sides / 2:
            valume = (sides-h) * v * 4
        else:
            valume = (sides - v) * (sides - h) * 4
    return valume
print(poc())
