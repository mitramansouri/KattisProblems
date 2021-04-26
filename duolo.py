def function():
    line = input().split()
    if int(line[1]) % 2 == 0:
        return 'Possible'
    else: return 'Impossible'
print(function())