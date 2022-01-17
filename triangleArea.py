def function():
    line_of_inputs = input().split()
    h = int(line_of_inputs[0])
    b = int(line_of_inputs[1])
    area = h*b/2
    return area
print(function())