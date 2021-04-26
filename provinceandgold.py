def function():
    list = input().split()
    for i in range(len(list)):
        list[i] = int(list[i])
    res = []
    gold = list[0] 
    silver = list[1] 
    copper = list[2]
    total = 3*gold + 2*silver + 1*copper
    if total <2:  #he can have one copper
        res += ['copper']
    elif total >= 8:  #he can have province or gold 
        res += ['Province or Gold']
    elif total >= 6:  # Duchy and Gold
        res += ['Duchy or Gold']
    elif total == 5: # 
        res += ['Duchy or Silver']
    elif total >= 3:
        res += ['Estate or Silver']
    elif total >= 2 :
        res += ['Estate or Copper']
    return res
print(*function())
    
        
        