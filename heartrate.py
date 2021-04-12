def heartRate():
    n = int(input())
    res=[]
    while (n):
        line_of_input = input()
        beats = int(line_of_input.split()[0])
        p = float(line_of_input.split()[1])
        abpm = 60 * beats / p
        q = 60 / p
        res += [abpm - q, abpm, abpm + q]
        n -= 1
    return res
def print_list(lst):
    for i in range(0,len(lst)-2,3):
        print(format(lst[i], '.4f'),format(lst[i+1], '.4f'),format(lst[i+2], '.4f'))


print_list(heartRate())