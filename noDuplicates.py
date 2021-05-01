def function():
    line = input().split()
    for i in line :
        if line.count(i) > 1:
            return 'yes'
    return 'no'
print(function())