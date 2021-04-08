def printer():
    n = int(input())
    temp = 0
    i = 0
    while (temp < n):
        temp = 2 ** i
        i += 1
    return i 
print(printer())
    
    
    
