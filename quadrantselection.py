def quadrant():
    x = int(input())
    y = int(input())
    if (x == 0 and y ==0 ):
        return 0
    if(x<0):
        #2 3
        if(y<0):
            return 3
        else :
            return 2
    if(x>0):
        #1 4
        if(y>0):
            return 1
        else :
            return 4
print(quadrant())