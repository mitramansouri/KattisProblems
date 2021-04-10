def chanukah():
    n = int(input())
    lst = []
    final = []
    while (n):
        line_of_input = input()
        res = line_of_input.split()
        lst.append(int(res[-1]))
        n -= 1
    for item in lst:
        a = [x for x in range(1, item + 1)]
        final_res = sum(a) + item
        final.append(final_res)
    return final
def print_list(lst):
    for i in range(len(lst)):
        print(str(i + 1) + " " + str(lst[i]))
        
print_list(chanukah())