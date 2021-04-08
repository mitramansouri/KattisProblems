def tarifa():
    megabytes = int(input())
    number_of_months = int(input())
    temp = number_of_months
    lst = []
    while (temp):
        lst.append(int(input()))
        temp -= 1
    sumation = sum(lst)
    res = megabytes + (megabytes * number_of_months) - sumation
    return res
print(tarifa())