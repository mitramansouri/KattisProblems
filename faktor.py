def faktor():
    line_of_input = input()
    first = line_of_input.split()[0]
    second = line_of_input.split()[1]
    return (int(first) * (int(second) - 1)) + 1
print(faktor())