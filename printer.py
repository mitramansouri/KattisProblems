
def printer(n):
    times = []
    r = 0
    if n == 1 :
        #should print
        times = "s"
        r = 1
        #return times 
    else :
        #make one printer and print
        times.append("p")
        #r += 1 
        times.append(printer(n-1))
        #r += printer(n-1)
    return times
#the number of nested lists are the number of efficent times , i guess tho 
print(printer(1))
