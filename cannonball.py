import math
def function():
    n = int(input())
    while (n):
        test_case = input().split()
        for i in range(len(test_case)):
            test_case[i] = float(test_case[i])
        print(safe_notsafe(test_case))
        n -= 1

def safe_notsafe(test_case):
    #len testcase is 5
    v0, theta, x1, h1, h2 = test_case
    t = x1 / (v0 * math.cos(math.radians(theta)))
    y = (v0 * t * math.sin(math.radians(theta))) - (1 / 2 * 9.81 * (t ** 2))
    if y >= h1 + 1 and y <= (h2 - 1):
        return 'Safe'
    else:
        return 'not safe'
function() 
    


