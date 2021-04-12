def hashed():
    n = input()
    sumi = sum_of_digits(n)
    if int(n) % sumi == 0:
        return n
    else:
        while (int(n) % sum_of_digits(n)):
            n = str(int(n) + 1)
        return n
         
def sum_of_digits(str):
    summation =0
    for i in range(len(str)):
        summation += int(str[i])
    return summation

print(hashed())