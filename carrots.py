def carrots():
    a = input()
    firtsinput = int(a.split()[0])
    while(firtsinput):
        b = input()
        firtsinput-=1
    return int(a.split()[1])
        
print(carrots())