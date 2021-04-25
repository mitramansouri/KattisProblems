def function():
    n = int(input())
    binary = bin(n)[2:]
    reversed_binary = reverse(binary)
    return int(reversed_binary, 2)

def reverse(str):
    reversed = ''
    for i in range(len(str)):
        reversed+= str[len(str) - 1 - i]
    return reversed
print(function())