def fizzbuzz():
    line_of_input = input()
    lst = line_of_input.split()
    counter = int(lst[-1])
    res = []
    fizz = int(lst[0])
    buzz = int(lst[1])
    for i in range(1,counter+1):
        if i % fizz == 0 and i % buzz == 0:
            res.append("FizzBuzz")
        elif i % fizz == 0:
            res.append("Fizz")
        elif i % buzz == 0:
            res.append("Buzz")
        else:
            res.append(i)
    return res
def print_list(lst):
    for i in lst:
        print(i)

print_list(fizzbuzz())
