def spam_detector():
    line_of_input = input()
    lenght = len(line_of_input)
    ratio_under_line_count = format(underline_detector(line_of_input)/lenght , '.16f')
    ratio_lower_case_count = format(n_lower_chars(line_of_input)/lenght ,'.16f')
    ratio_upper_case_count = format(n_upper_chars(line_of_input)/lenght ,'.16f')
    ratio_ascii = format(ascii_detector(line_of_input)/lenght ,'.16f')
    print(ratio_under_line_count)
    print(ratio_lower_case_count)
    print(ratio_upper_case_count)
    print(ratio_ascii)

def n_lower_chars(str):
    return sum(1 for c in str if c.islower())

def n_upper_chars(str):
    return sum(1 for c in str if c.isupper())

def underline_detector(str):
    count = 0
    for i in str:
        if i == "_":
            count += 1
    return count
def ascii_detector(str):
    count = 0
    for i in str:
        if ord(i) >= 33 and ord(i) <= 126:
            #i is not an uppercase word
            if not (ord(i)>=65 and ord(i)<= 90):
                #i is not a lower case word
                if not (ord(i)>=97 and ord(i)<=122):
                    #if i != '_'
                    if i!= '_' :
                        count+=1
    return count

spam_detector()