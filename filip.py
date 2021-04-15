def filip():
    line_of_input = input()
    one = line_of_input.split()[0]
    two = line_of_input.split()[1]
    fliped = max(int(reverse(one)), int(reverse(two)))
    return fliped
    

def reverse(str):
    reversed_str = ''
    last = len(str)
    for i in range(last):
        reversed_str+= str[last - i - 1]
    return reversed_str
print(filip())

