def zamka():
    l = int(input())
    d = int(input())
    x = int(input())
    lst = []
    for i in range(l, d + 1):
        if sum_of_digits(i) == x:
            lst.append(i)
    return lst
        
    
def sum_of_digits(n):
    temp = n
    sum = 0 
    while (temp > 0):
        r = temp%10
        temp = temp//10

        sum += r
    return sum

def printt(lst):
    print(lst[0])
    print(lst[-1])
printt(zamka())