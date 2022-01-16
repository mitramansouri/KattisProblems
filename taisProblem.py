def function():
    n = int(input())
    i = 0
    dic = {}
    while(n>0):
        inputs = input().split()
        ms = int(inputs[0])
        volume = float(inputs[1])
        dic[i] = (ms, volume)
        n -= 1
        i += 1
    area = 0 
    for i in range(len(dic)-1) :
        a = dic[i][0]
        b = dic[i+1][0]
        c = dic[i][1]
        d = dic[i+1][1]
        area += (abs(a-b))*(c+d)/2000 
    return area

print(function())       