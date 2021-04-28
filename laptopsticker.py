def laptop():
    line = input().split()
    wc, hc, ws, hs = line
    if int(wc) - int(ws) >= 2 and int(hc) - int(hs) >= 2:
        # if int(wc)- int(hs) >= 2 and int(hc) - int(ws) >= 2:
        return 1
    else: return 0
print(laptop())