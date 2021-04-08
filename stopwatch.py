def stopwatch():
    times_clicked = int(input())

    temp = times_clicked
    lst = []
    while (temp):
        lst.append(int(input()))
        temp-=1
    i = 0
    list2 = []
    
    if not times_clicked % 2 == 0:
        return "still running"
    else:
        while (i < times_clicked):
            list2.append(lst[i + 1] - lst[i])
            i += 2
        return sum(list2)

print(stopwatch())