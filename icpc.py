def function():
    n = int(input())
    dic = {}
    
    while (n):
        line = input().split()
        if line[0] not in dic :
            dic[line[0]] = line[1]
        else:
            pass
        n -= 1
    count = 0
    for i in dic:
        if count < 12:
            print('{} {}'.format(i, dic[i]))
            count +=1


function()
