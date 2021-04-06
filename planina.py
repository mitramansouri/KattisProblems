iterations = int(input())

def planina(n):
    #default
    
    if n == 1 :
        res = 3
    else :
        res = (planina(n-1) + 2**(n-1))
    return res


print(planina(iterations)**2)
    