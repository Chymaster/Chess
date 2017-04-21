import random
global record
record = []
def start():
    global legal
    legal = None
    global round
    round = 'white'
    global possibility
    possibility = []
    global takeover
    takeover = []
    global state
    state = None
    global mpiece
    mpiece = None
    global lbr   #each list is one piece in format
    lbr = ['lbr',1,8,'r']   #piecename = ['piecename', position(x-axis),position(y-axis),'piecetype']
    global lbk
    lbk = ['lbk',2,8,'n']       #points:
    global lbb
    lbb = ['lbb',3,8,'b']       #pawn in white side and black side have different moving ways, so they have to be identified
    global bq
    bq = ['bq ',4,8,'q']         #mpiece is the variable that indicates which piece is moving, it's the index number in white/black
    global bk
    bk = ['bk ',5,8,'k']         #
    global rbb
    rbb = ['rbb',6,8,'b']       #
    global rbk
    rbk = ['rbk',7,8,'n']
    global rbr
    rbr = ['rbr',8,8,'r']
    global bp1
    bp1 = ['bp1',1,7,'bp']
    global bp2
    bp2 = ['bp2',2,7,'bp']
    global bp3
    bp3 = ['bp3',3,7,'bp']
    global bp4
    bp4 = ['bp4',4,7,'bp']
    global bp5
    bp5 = ['bp5',5,7,'bp']
    global bp6
    bp6 = ['bp6',6,7,'bp']
    global bp7
    bp7 = ['bp7',7,7,'bp']
    global bp8
    bp8 = ['bp8',8,7,'bp']

    global lwr
    lwr = ['lwr',1,1,'r']
    global lwk
    lwk = ['lwk',2,1,'n']
    global lwb
    lwb = ['lwb',3,1,'b']
    global wq
    wq = ['wq ',4,1,'q']
    global wk
    wk = ['wk ',5,1,'k']
    global rwb
    rwb = ['rwb',6,1,'b']
    global rwk
    rwk = ['rwk',7,1,'n']
    global rwr
    rwr = ['rwr',8,1,'r']
    global wp1
    wp1 = ['wp1',1,2,'wp']
    global wp2
    wp2 = ['wp2',2,2,'wp']
    global wp3
    wp3 = ['wp3',3,2,'wp']
    global wp4
    wp4 = ['wp4',4,2,'wp']
    global wp5
    wp5 = ['wp5',5,2,'wp']
    global wp6
    wp6 = ['wp6',6,2,'wp']
    global wp7
    wp7 = ['wp7',7,2,'wp']
    global wp8
    wp8 = ['wp8',8,2,'wp']
    global strwhite
    global strblack
    strwhite = ['lwr','lwk','lwb','wq ','wk ','rwb','rwk','rwr','wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']
    strblack = ['lbr','lbk','lbb','bq ','bk ','rbb','rbk','rbr','bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8']
start()
def statestrlist(whichround):  #Tool to define which pieces to eat
    if whichround == 'white':       #generally reverse and return the opposite str list
        return strblack
    elif whichround == 'black':
        return strwhite


def po(x,y,s):      #po is the def for position in chessboard, returns piece or blank
    global cb
    for i in cb:
        if i[1] == x and i[2] == y:
            return i[s]
    return '   '

def chessboard():
    print(po(1,8,0),po(2,8,0),po(3,8,0),po(4,8,0),po(5,8,0),po(6,8,0),po(7,8,0),po(8,8,0))
    print(po(1,7,0),po(2,7,0),po(3,7,0),po(4,7,0),po(5,7,0),po(6,7,0),po(7,7,0),po(8,7,0))
    print(po(1,6,0),po(2,6,0),po(3,6,0),po(4,6,0),po(5,6,0),po(6,6,0),po(7,6,0),po(8,6,0))
    print(po(1,5,0),po(2,5,0),po(3,5,0),po(4,5,0),po(5,5,0),po(6,5,0),po(7,5,0),po(8,5,0))
    print(po(1,4,0),po(2,4,0),po(3,4,0),po(4,4,0),po(5,4,0),po(6,4,0),po(7,4,0),po(8,4,0))
    print(po(1,3,0),po(2,3,0),po(3,3,0),po(4,3,0),po(5,3,0),po(6,3,0),po(7,3,0),po(8,3,0))
    print(po(1,2,0),po(2,2,0),po(3,2,0),po(4,2,0),po(5,2,0),po(6,2,0),po(7,2,0),po(8,2,0))
    print(po(1,1,0),po(2,1,0),po(3,1,0),po(4,1,0),po(5,1,0),po(6,1,0),po(7,1,0),po(8,1,0))
    print(round)
    print('\n')

def fresh():
    global cb
    global white
    global black
    cb = [lwr,lwk,lwb,wq,wk,rwb,rwk,rwr,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,lbr,lbk,lbb,bq,bk,rbb,rbk,rbr,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]
    white = [lwr,lwk,lwb,wq,wk,rwb,rwk,rwr,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8]
    strwhite = ['lwr','lwk','lwb','wq ','wk ','rwb','rwk','rwr','wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']
    black = [lbr,lbk,lbb,bq,bk,rbb,rbk,rbr,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]
    strblack = ['lbr','lbk','lbb','bq ','bk ','rbb','rbk','rbr','bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8']
fresh()
def rule():
    global possibility
    possibility = []
    global notation
    global state
    global mpiece
    global round
    if round == 'white':
        for i in white:
            if i[1] == notation[0] and i[2] == notation[1]:
                state = i[3]     #state shows which type of piece is moving
                mpiece = i[0]    #mpiece shows which chess is moving
                print(mpiece)
                if state == 'wp':            #RULES  ADD HERE
                    wpawnrule()
                if state == 'r':
                    rrule()
                if state == 'q':
                    qrule()
                if state == 'b':
                    brule()
                if state == 'n':
                    nrule()
                if state == 'k':
                    krule()
                for l in possibility:
                    if l/100 == l - l / 100 * 100:
                        possibility.remove(l)
                print(possibility)
                #print(notation[0]*1000+notation[1]*100+notation[2]*10+notation[3])
                if notation[0]*1000+notation[1]*100+notation[2]*10+notation[3] in possibility:
                    print('legal move')
                    print(takeover)
                    record.append('move(%r)'%str(notation[0]*1000+notation[1]*100+notation[2]*10+notation[3]))
                    if notation[2]*10+notation[3] in takeover:
                        takenover = po(notation[2],notation[3],0)
                        if takenover == 'bk ':
                            takenover = 'bk'
                        elif takenover == 'bq ':
                            takenover = 'bq'
                        exec('globals()[%r] = [None,0,0,None]'%takenover)
                        #print(globals()[takenover])
                        fresh()
                    if i[0] == 'lwr':
                        lwr[1] = notation[2]
                        lwr[2] = notation[3]
                    elif i[0] == 'lwk':
                        lwk[1] = notation[2]
                        lwk[2] = notation[3]
                    elif i[0] == 'lwb':
                        lwb[1] = notation[2]
                        lwb[2] = notation[3]
                    elif i[0] == 'wq ':
                        wq[1] = notation[2]
                        wq[2] = notation[3]
                    elif i[0] == 'wk ':
                        wk[1] = notation[2]
                        wk[2] = notation[3]
                    elif i[0] == 'rwb':
                        rwb[1] = notation[2]
                        rwb[2] = notation[3]
                    elif i[0] == 'rwk':
                        rwk[1] = notation[2]
                        rwk[2] = notation[3]
                    elif i[0] == 'rwr':
                        rwr[1] = notation[2]
                        rwr[2] = notation[3]
                    elif i[0] == 'wp1':
                        wp1[1] = notation[2]
                        wp1[2] = notation[3]
                    elif i[0] == 'wp2':
                        wp2[1] = notation[2]
                        wp2[2] = notation[3]
                    elif i[0] == 'wp3':
                        wp3[1] = notation[2]
                        wp3[2] = notation[3]
                    elif i[0] == 'wp4':
                        wp4[1] = notation[2]
                        wp4[2] = notation[3]
                    elif i[0] == 'wp4':
                        wp4[1] = notation[2]
                        wp4[2] = notation[3]
                    elif i[0] == 'wp5':
                        wp5[1] = notation[2]
                        wp5[2] = notation[3]
                    elif i[0] == 'wp6':
                        wp6[1] = notation[2]
                        wp6[2] = notation[3]
                    elif i[0] == 'wp7':
                        wp7[1] = notation[2] 
                        wp7[2] = notation[3]
                    elif i[0] == 'wp8':
                        wp8[1] = notation[2]
                        wp8[2] = notation[3]
                    round = 'black'
                    fresh()
                    chessboard()
                else:
                    print('Illegal move,, please check')
    elif round == 'black':
        for i in black:
            if i[1] == notation[0] and i[2] == notation[1]:
                state = i[3]
                mpiece = black.index(i)
                print(mpiece)
                if state == 'bp':            #RULES  ADD HERE
                    bpawnrule()
                if state == 'r':
                    rrule()
                if state == 'q':
                    qrule()
                if state == 'b':
                    brule()
                if state == 'n':
                    nrule()
                if state == 'k':
                    krule()
                for l in possibility:
                    if l/100 == l - l / 100 * 100:
                        possibility.remove(l)
                print(possibility)
                if notation[0]*1000+notation[1]*100+notation[2]*10+notation[3] in possibility:
                    print('legal move')
                    record.append('move(%r)'%str(notation[0]*1000+notation[1]*100+notation[2]*10+notation[3]))
                    if notation[2]*10+notation[3] in takeover: # takeover part for black
                        #print('triggered')
                        takenover = po(notation[2],notation[3],0)
                        if takenover == 'wk ':
                            takenover = 'wk'
                        elif takenover == 'wq ':
                            takenover = 'wq'
                        #print(takenover)
                        exec('globals()[%r] = [None,0,0,None]'%takenover)
                        #print(globals()[takenover])
                    if i[0] == 'lbr':
                        lbr[1] = notation[2]
                        lbr[2] = notation[3]
                    elif i[0] == 'lbk':
                        lbk[1] = notation[2]
                        lbk[2] = notation[3]
                    elif i[0] == 'lbb':
                        lbb[1] = notation[2]
                        lbb[2] = notation[3]
                    elif i[0] == 'bq ':
                        bq[1] = notation[2]
                        bq[2] = notation[3]
                    elif i[0] == 'bk ':
                        bk[1] = notation[2]
                        bk[2] = notation[3]
                    elif i[0] == 'rbb':
                        rbb[1] = notation[2]
                        rbb[2] = notation[3]
                    elif i[0] == 'rbk':
                        rbk[1] = notation[2] 
                        rbk[2] = notation[3]
                    elif i[0] == 'rbr':
                        rbr[1] = notation[2]
                        rbr[2] = notation[3]
                    elif i[0] == 'bp1':
                        bp1[1] = notation[2]
                        bp1[2] = notation[3]
                    elif i[0] == 'bp2':
                        bp2[1] = notation[2]
                        bp2[2] = notation[3]
                    elif i[0] == 'bp3':
                        bp3[1] = notation[2]
                        bp3[2] = notation[3]
                    elif i[0] == 'bp4':
                        bp4[1] = notation[2]
                        bp4[2] = notation[3]
                    elif i[0] == 'bp4':
                        bp4[1] = notation[2]
                        bp4[2] = notation[3]
                    elif i[0] == 'bp5':
                        bp5[1] = notation[2]
                        bp5[2] = notation[3]
                    elif i[0] == 'bp6':
                        bp6[1] = notation[2]
                        bp6[2] = notation[3]
                    elif i[0] == 'bp7':
                        bp7[1] = notation[2]
                        bp7[2] = notation[3]
                    elif i[0] == 'bp8':
                        bp8[1] = notation[2]
                        bp8[2] = notation[3]
                    round = 'white'
                    fresh()
                    chessboard()
                else:
                    print('illegal move')
    if wk == [None,0,0,None] or bk == [None,0,0,None]:
        print(''.join([round,' lost']))
        print('Game over, please start again')
        start()
def move(x):
    global notation
    global state
    notation = [int(i) for i in str(x)]
    rule()
    
def wpawnrule():
    global legal
    global possibility
    global takeover
    global strblack
    if po(notation[0],notation[1]+1,0) == '   ':
        possibility.append(notation[0]*1000+notation[1]*100+notation[0]*10 + notation[1] + 1)
    if po(notation[0],notation[1]+2,0) == '   ' and notation[1] == 2:
        possibility.append(notation[0]*1000+notation[1]*100+notation[0]*10 + notation[1] + 2)
    if po(notation[0]-1,notation[1] + 1,0) in strblack:
        possibility.append(notation[0]*1000+notation[1]*100+(notation[0]-1)*10 + notation[1] + 1)
        takeover.append((notation[0]-1)*10 + notation[1] + 1)
    if po(notation[0]+1,notation[1] + 1,0) in strblack:
        possibility.append(notation[0]*1000+notation[1]*100+(notation[0]+1)*10 + notation[1] + 1)
        takeover.append((notation[0]+1)*10 + notation[1] + 1)
    if (notation[0]*1000+notation[1]*100+notation[2]*10+notation[3]) in possibility:
        if notation[3] == 8:
            exec("globals()[%r][3] = ['q']"%po(notation[0],notation[1],0))
    #print(possibility)
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
    #print(possibility)
def rrule():
    global legal
    global possibility
    global takeover

    L = [0,9]   
    x = notation[0]
    y = notation[1]
    for i in cb:
        if i[2] == y:
            L.append(i[1]) # all notation in y = i[2] line (seen position 0 and 9 as a piece to block out)
    L.sort()
    #print(L)
    #print(L[L.index(x)-1])
    Lx=range(int(L[L.index(x)-1]),int(L[L.index(x)+1]))
    Lx.pop(0)
    for a in Lx:
        possibility.append(notation[0]*1000+notation[1]*100+a*10+y)
    if po(int(L[L.index(x)-1]),y,0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+int(L[L.index(x)-1])*10+y)
        takeover.append(int(L[L.index(x)-1])*10+y)
    if po(int(L[L.index(x)+1]),y,0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+int(L[L.index(x)+1]*10)+y)
        takeover.append(int(L[L.index(x)+1]*10)+y)

    L = [0,9]    
    for i in cb:
        if i[1] == x:
            L.append(i[2])
    L.sort()
    #print(L)
    Ly=range(int(L[L.index(y)-1]),int(L[L.index(y)+1]))
    Ly.pop(0)
    for a in Ly:
        possibility.append(notation[0]*1000+notation[1]*100+x*10+a)
    #print(int(L[L.index(y)-1]))
    #print(y)
    po(x,int(L[L.index(y)-1]),0)
    #print(statestrlist(round))
    if po(x,int(L[L.index(y)-1]),0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+x*10+int(L[L.index(y)-1]))
        takeover.append(x*10+int(L[L.index(y)-1]))
    if po(x,int(L[L.index(y)+1]),0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+x*10+int(L[L.index(y)+1]))
        takeover.append(x*10+int(L[L.index(y)+1]))


def qrule():   # the new queen rule based on rook 
    global legal
    global possibility
    global takeover

#This is vertical and horizontal line
    L = [0,9]   
    x = notation[0]
    y = notation[1]
    for i in cb:
        if i[2] == y:
            L.append(i[1])
    L.sort()
    #print(L)
    #print(L[L.index(x)-1])
    Lx=range(int(L[L.index(x)-1]),int(L[L.index(x)+1]))
    Lx.pop(0)
    for a in Lx:
        possibility.append(notation[0]*1000+notation[1]*100+a*10+y)
    if po(int(L[L.index(x)-1]),y,0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+int(L[L.index(x)-1])*10+y)
        takeover.append(int(L[L.index(x)-1])*10+y)
    if po(int(L[L.index(x)+1]),y,0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+int(L[L.index(x)+1]*10)+y)
        takeover.append(int(L[L.index(x)+1]*10)+y)


    L = [0,9]    
    for i in cb:
        if i[1] == x:
            L.append(i[2])
    L.sort()
    #print(L)
    Ly=range(int(L[L.index(y)-1]),int(L[L.index(y)+1]))
    Ly.pop(0)
    for a in Ly:
        possibility.append(notation[0]*1000+notation[1]*100+x*10+a)
    #print(int(L[L.index(y)-1]))
    #print(y)
    po(x,int(L[L.index(y)-1]),0)
    #print(statestrlist(round))
    if po(x,int(L[L.index(y)-1]),0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+x*10+int(L[L.index(y)-1]))
        takeover.append(x*10+int(L[L.index(y)-1]))       
    if po(x,int(L[L.index(y)+1]),0) in statestrlist(round):
        possibility.append(notation[0]*1000+notation[1]*100+x*10+int(L[L.index(y)+1]))
        takeover.append(x*10+int(L[L.index(y)+1]))

    
# the rook rule ends here
# the bishop rule starts here
    x = notation[0]
    y = notation[1]
    c = y + x                         #in chessboard:
    #downwards
    if c >= 9:
        L = [[c-9,9],[9,c-9]]
    elif c <= 7:
        L = [[0,c],[c,0]]
    elif c == 8:
        L = [[0,9],[9,0]]
    for i in range(1,9):
       #the biggest of possible x is 8
        #x and y can't be bigger than 8 and smaller than 1
        if max(i,-i+c)<= 8 and min(i,-i+c)>=1:
            L.append([i,-i+c])
    L.sort()
    if c >= 9:
        list_of_existing_piece = [[c-9,9],[9,c-9]]
    elif c <= 7:
        list_of_existing_piece = [[0,c],[c,0]]
    elif c == 8:
        list_of_existing_piece = [[0,9],[9,0]]
    for i in cb:
        if i[1] + i[2] == c:
            list_of_existing_piece.append([i[1],i[2]])
    list_of_existing_piece.sort()
    moving_range = []
    for a in range(L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])-1])+1,L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])+1])):
        moving_range.append(L[a])
    for a in moving_range:
        possibility.append(x*1000+y*100+a[0]*10+a[1])
    #all in range possibilities
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
    #include the take overs
    #print(possibility)

##upward
    L=[]
    c = y - x
    if c <= -1:
        L = [[-c,0],[9,9-c]]
    elif c >= 1:
        L = [[0,c],[9-c,9]]
    elif c == 0:
        L = [[0,0],[9,9]]
    for i in range(1,9):
        if max(i,i+c)<=8 and min(i,i+c)>=1:
            L.append([i,i+c])
    L.sort()
    if c <= -1:
        list_of_existing_piece = [[-c,0],[9,9-c]]
    elif c >= 1:
        list_of_existing_piece = [[0,c],[9-c,9]]
    elif c == 0:
        list_of_existing_piece = [[0,0],[9,9]]
    for i in cb:
        if i[2] - i[1] == c:
            list_of_existing_piece.append([i[1],i[2]]) 
    list_of_existing_piece.sort()
    moving_range = []
    for a in range(L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])-1])+1,L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])+1])):
        moving_range.append(L[a])
    #possibility.append(x*1000+y*100+a[0]*10+a[1]) for a in moving_range)
    #print(moving_range)
    for a in moving_range:
        possibility.append(x*1000+y*100+a[0]*10+a[1]) 
    #all in range possibilities
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
    #include the take overs

def brule():
    global legal
    global possibility
    global takeover
    

    x = notation[0]
    y = notation[1]
    c = y + x                         #in chessboard:
    #downwards
    if c >= 9:
        L = [[c-9,9],[9,c-9]]
    elif c <= 7:
        L = [[0,c],[c,0]]
    elif c == 8:
        L = [[0,9],[9,0]]
    for i in range(1,9):
       #the biggest of possible x is 8
        #x and y can't be bigger than 8 and smaller than 1
        if max(i,-i+c)<= 8 and min(i,-i+c)>=1:
            L.append([i,-i+c])
    L.sort()
    if c >= 9:
        list_of_existing_piece = [[c-9,9],[9,c-9]]
    elif c <= 7:
        list_of_existing_piece = [[0,c],[c,0]]
    elif c == 8:
        list_of_existing_piece = [[0,9],[9,0]]
    for i in cb:
        if i[1] + i[2] == c:
            list_of_existing_piece.append([i[1],i[2]])
    list_of_existing_piece.sort()
    moving_range = []
    for a in range(L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])-1])+1,L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])+1])):
        moving_range.append(L[a])
    for a in moving_range:
        possibility.append(x*1000+y*100+a[0]*10+a[1])
    #all in range possibilities
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
    #include the take overs

##upward
    c = y - x
    if c <= -1:
        L = [[-c,0],[9,9+c]]
    elif c >= 1:
        L = [[0,c],[9-c,9]]
    elif c == 0:
        L = [[0,0],[9,9]]
    for i in range(1,9):
        if max(i,i+c)<=8 and min(i,i+c)>=1:
            L.append([i,i+c])
    L.sort()
    #print(L)
    if c <= -1:
        list_of_existing_piece = [[-c,0],[9,9+c]]
    elif c >= 1:
        list_of_existing_piece = [[0,c],[9-c,9]]
    elif c == 0:
        list_of_existing_piece = [[0,0],[9,9]]
    for i in cb:
        if i[2] - i[1] == c:
            list_of_existing_piece.append([i[1],i[2]]) 
    list_of_existing_piece.sort()
    moving_range = []
    for a in range(L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])-1])+1,L.index(list_of_existing_piece[list_of_existing_piece.index([x,y])+1])):
        moving_range.append(L[a])
    #possibility.append(x*1000+y*100+a[0]*10+a[1]) for a in moving_range)
    for a in moving_range:
        possibility.append(x*1000+y*100+a[0]*10+a[1]) 
    #all in range possibilities
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])+1][1])
    if po(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0],list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1],0) in statestrlist(round):
        takeover.append(list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
        possibility.append(x*1000+y*100+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][0]*10+list_of_existing_piece[list_of_existing_piece.index([x,y])-1][1])
    #include the take overs

def nrule():
    global possibility
    global takeover
    x = notation[0]
    y = notation[1]
    L = []
    L1 = [notation[0]+1,notation[0]-1,notation[0]+2,notation[0]-2]
    L2 = [notation[1]+1,notation[1]-1,notation[1]+2,notation[1]-2]
    for a in L1:
        if a in range(1,9):
            for b in L2:
                if b in range(1,9):
                    if abs(a- x) != abs(b - y):
                        L.append([a,b])
    for a in L:

        if po(a[0],a[1],0) == '   ':
            possibility.append(x*1000+y*100+a[0]*10+a[1])
        elif po(a[0],a[1],0) in statestrlist(round):
            possibility.append(x*1000+y*100+a[0]*10+a[1])
            takeover.append(a[0]*10+a[1])
        
def krule():
    global possibility
    global takeover

    x = notation[0]
    y = notation[1]
    L = []
    L1 = (range(x-1,x+2))
    L2 = (range(y-1,y+2))
    for a in L1:
        if a in range(1,9):
            for b in L2:
                if b in range(1,9):
                    L.append([a,b])
    for a in L:
        if po(a[0],a[1],0) == '   ':
            possibility.append(x*1000+y*100+a[0]*10+a[1])
        elif po(a[0],a[1],0) in statestrlist(round):
            possibility.append(x*1000+y*100+a[0]*10+a[1])
            takeover.append(a[0]*10+a[1])
        
def Score(piece):
    if piece == 'wp':
        return 1
    elif piece == 'bp':
        return 1
    elif piece == 'n':
        return 5
    elif piece == 'r':
        return 20
    elif piece == 'b':
        return 10
    elif piece == 'q':
        return 50
    elif piece == 'k':
        return 100
                
def AI():
    global possibility
    possibility = []
    global notation
    notation = [0,0,5,5]
    global state
    prior = []
    global mpiece
    global white
    global black
    global round
    if round == 'white':
        for i in white:
            notation[0] = i[1]
            notation[1] = i[2]
            state = i[3]     #state shows which type of piece is moving
            mpiece = i[0]    #mpiece shows which chess is moving
            if state == 'wp':            #RULES  ADD HERE
                wpawnrule()
            if state == 'r':
                rrule()
            if state == 'q':
                qrule()
            if state == 'b':
                brule()
            if state == 'n':
                nrule()
            if state == 'k':
                krule()
            for l in possibility:
                if l/100 == l - l / 100 * 100:
                    possibility.remove(l)
        prior = []
        current_score = 0
        for moves in possibility:
            smoves = [int(a) for a in str(moves)]
            if po(smoves[2],smoves[3],0) in strblack:
                if int(current_score) < int(Score(po(smoves[2],smoves[3],3))):
                    current_score = Score(po(smoves[2],smoves[3],3))
                    prior = smoves
                elif current_score == Score(po(smoves[2],smoves[3],3)):
                    choice = random.randint(0,1)
                    if choice == 0:
                        prior = smoves
        print(prior)
        if len(prior) == 0:
            move(random.choice(possibility))
        else:
            move(int(''.join(str(a) for a in prior)))

    elif round == 'black':
        for i in black:
            notation[0] = i[1]
            notation[1] = i[2]
            state = i[3]     #state shows which type of piece is moving
            mpiece = i[0]    #mpiece shows which chess is moving
            if state == 'wp':            #RULES  ADD HERE
                bpawnrule()
            if state == 'r':
                rrule()
            if state == 'q':
                qrule()
            if state == 'b':
                brule()
            if state == 'n':
                nrule()
            if state == 'k':
                krule()
            for l in possibility:
                if l/100 == l - l / 100 * 100:
                    possibility.remove(l)
        prior = []
        current_score = 0
        for moves in possibility:
            smoves = [int(a) for a in str(moves)]
            if po(smoves[2],smoves[3],0) in strwhite:
                if current_score < Score(po(smoves[2],smoves[3],3)):
                    current_score = Score(po(smoves[2],smoves[3],3))
                    prior = smoves
                elif current_score == Score(po(smoves[2],smoves[3],3)):
                    choice = random.randint(0,1)
                    if choice == 1:
                        prior = smoves
        if len(prior) == 0:
            move(random.choice(possibility))
        else:
            move(int(''.join(str(a) for a in prior)))





def test():     #this is a test base
    global rwr
    rwr = ['rwr',1,6,'r']
    fresh()
    while 1:
        raw_input('Press any key to continue')
        AI()
#while fin == False:
    
        
        
        
