def function():
    n = int(input())
    line_of_input = input().split()
    sum = 0
    count = 0
    for i in range(n):
        if int(line_of_input[i]) >= 0:
            sum += int(line_of_input[i])
            count += 1
            
    return sum / count
print(function())

    