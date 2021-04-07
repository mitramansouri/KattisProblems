def degree():
    n = int(input())
    degrees = input()
    degrees_list = degrees.split()
    res = 0
    for i in degrees_list :
        if int(i) < 0:
            res+=1
    return res

print(degree())