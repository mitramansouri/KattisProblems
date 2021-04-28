def numberfun():
    n = int(input())
    while (n):
        line = input().split()
        for i in range(len(line)):
            line[i] = int(line[i])
        # check 
        if line[1] + line[0] == line[2]:
            print( 'Possible')
        elif abs(line[0] - line[1]) == abs(line[2]):
            print( 'Possible')
        elif line[0] * line[1] == line[2]:
            print( 'Possible')
        elif line[0] / line[1] == line[2] or line[1] / line[0] == line[2]:
            print( 'Possible')
        else:
            print('Impossible')
        n -= 1
    
numberfun()