def dicecup():
    line_of_input = input()
    first = int(line_of_input.split()[0])
    second = int(line_of_input.split()[1])
    if first == second:
        return first + 1
    else:
    num_of_ans = abs(a-b)+1
    start = min(a,b)+1
    for i in range(start,start+num_of_ans):
        print(i)
print(dicecup())