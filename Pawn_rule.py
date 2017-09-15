def bpawnrule():
    global legal
    global possibility
    global takeover
    global strwhite
    if po(notation[0],notation[1]-1,0) == '   ':
        possibility.append(notation[0]*1000+notation[1]*100+notation[0]*10 + notation[1] - 1)
    if po(notation[0],notation[1]-2,0) == '   ' and notation[1] == 7:
        possibility.append(notation[0]*1000+notation[1]*100+notation[0]*10 + notation[1] - 2)
    if po(notation[0]-1,notation[1] - 1,0) in strwhite:    #takeover
        possibility.append(notation[0]*1000+notation[1]*100+(notation[0]-1)*10 + notation[1] - 1)
        takeover.append((notation[0]-1)*10 + notation[1] - 1)
    if po(notation[0]+1,notation[1] - 1,0) in strwhite:     #takeover
        possibility.append(notation[0]*1000+notation[1]*100+(notation[0]+1)*10 + notation[1] - 1)
        takeover.append((notation[0]+1)*10 + notation[1] - 1)
    if (notation[0]*1000+notation[1]*100+notation[2]*10+notation[3]) in possibility:
        if notation[3] == 1:
            exec("globals()[%r][3] = ['q']"%po(notation[0],notation[1],0))
