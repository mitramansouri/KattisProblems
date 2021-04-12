def forcedChoice():
    line_of_input = input()
    n = int(line_of_input.split()[2])
    cards = [str(x) for x in range(1,int(line_of_input.split()[0])+1)]
    ans =[]
    while (n):
        line = input().split()[1:]
        if line_of_input.split()[1] in line:
            ans.append('kEEP')
        else:
            for i in line:
                cards.remove(i)
            ans.append("REMOVE")
        n-=1
    return ans
def print_list(lst):
    for i in lst:
        print(i)
print_list(forcedChoice())