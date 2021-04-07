def jol():
    list = input()
    list_items = list.split()
    product = 1
    for i in list_items:
        product = product*int(i)
    return product
    
print(jol())