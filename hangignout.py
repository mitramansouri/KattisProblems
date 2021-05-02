def function():
    line = input().split()
    l = int(line[0])
    number_of_events = int(line[1])
    total = 0
    not_allowed = 0
    while (number_of_events):
        statement = input().split()
        if statement[0] == 'enter':
            if total + int(statement[1]) <= l:
                total += int(statement[1])
            else:
                not_allowed += 1
        elif statement[0] == 'leave':
            total -= int(statement[1])
        number_of_events -= 1
    return not_allowed
print(function()) 