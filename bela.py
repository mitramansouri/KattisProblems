def bela():
    line_of_input =  input()
    sets = int(line_of_input.split()[0])
    dominant = line_of_input.split()[1]
    dom_dic = {"A":11 , "K":4 , "Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
    non_dom_dic = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
    res = 0
    while (sets):
        i = 0
        while (i < 4):
            key = input()
            if key[1] == dominant:
                res += dom_dic[key[0]]
            else:
                res += non_dom_dic[key[0]]
            i += 1
        sets -= 1
    return res
print(bela())


