def function():
    n = int(input())
    output = []
    while (n):
        line = input()
        if 'Simon says' in line:
            output.append(' '.join(line.split()[2:]))
        n -= 1
    return output
print(*function(),sep='\n')