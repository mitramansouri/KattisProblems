import math

def function():
    res = []
    line = input()
    while (line != '0 0 0'):
        radius = float(line.split()[0])
        exact_area = radius** 2 * math.pi
        estimated_area = float(line.split()[2]) / float(line.split()[1]) * (radius * 2)** 2
        res.append('{} {}'.format(exact_area, estimated_area))
        line = input()
    return res
print(*function(), sep='\n')
        