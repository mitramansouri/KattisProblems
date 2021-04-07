def autor():
    a = input()
    a_list = a.split("-")
    res = ""
    for i in a_list:
        res+=i[0]
    return res
print(autor())