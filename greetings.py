def greeting():
    a = input()
    es = 0
    for i in a :
        if i == "e":
            es +=1
            
    res = a[0] + es*2*"e"+ a[-1]
    return res

print(greeting())