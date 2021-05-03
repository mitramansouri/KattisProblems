import math
def function():
    a, b, c, d = input().split()
    a, b, c, d = float(a), float(b), float(c), float(d)
    s = (a + b + c + d) / 2
    return math.sqrt((s - a)*(s - b)*(s - c)*(s - d))
print(function())
