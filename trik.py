def function():
    list = ['ball' , '1' , '1']
    line = input()
    for i in line:
        if i == 'A': #swap zero and one
            list[0], list[1] = list[1] , list[0]
        elif i == "B": #swap one and two
            list[1], list[2] = list[2] , list[1]
        elif i == 'C': #swap two and zero
            list[0], list[2] = list[2], list[0]
    return list.index('ball')+1

print(function())