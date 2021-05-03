def function():
    line = input().split()
    if int(line[0]) == 0 and int(line[1]) == 0:  #or == 0 
        return 'Not a moose'
    elif int(line[0]) == int(line[1]):
        return 'Even {}'.format(2*int(line[0]))
    else:
        return 'Odd {}'.format(2*max(int(line[0]), int(line[1])))
print(function())