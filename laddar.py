import math
def ladder():
    line_of_input = input()
    h = int(line_of_input.split()[0])
    degree = int(line_of_input.split()[1])
    return math.ceil(h / math.sin(math.radians(degree)))
    
print(ladder())