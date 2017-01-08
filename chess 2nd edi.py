global round
round = 'white'
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
bq = ['bq',4,8,'q']         #mpiece is the variable that indicates which piece is moving, it's the index number in white/black
global bk
bk = ['bk',5,8,'k']         #
global rbb
rbb = ['rbb',6,8,'b']       #
global rbk
rbk = ['rbk',7,8,'n']
global rbr
rbr = ['rbr',8,8,'r']
global bp8
bp1 = ['bp1',1,7,'bp']
global bp7
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
wq = ['wq',4,1,'q']
global wk
wk = ['wk',5,1,'k']
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

def fresh():
    global cb
    global white
    global black
    cb = [lwr,lwk,lwb,wq,wk,rwb,rwk,rwr,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,lbr,lbk,lbb,bq,bk,rbb,rbk,rbr,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]
    white = [lwr,lwk,lwb,wq,wk,rwb,rwk,rwr,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8]
    black = [lbr,lbk,lbb,bq,bk,rbb,rbk,rbr,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8]
fresh()
def rule():
    global notation
    if round == 'white':
        for i in white:
            print(i[1],i[2])
            print(notation[0],notation[1])
            if i[1] == notation[0] and i[2] == notation[1]:
                state = i[3]     #state shows which type of piece is moving
                mpiece = white.index(i)    #mpiece shows which chess is moving
                print(state)
                #!!!!!!! RULE FOR EACH PIECE START HERE
    elif round == 'black':
        for i in black:
            print(i[1],i[1])
            print(notation[0],notation[1])
            if i[1] == notation[0] and i[2] == notation[1]:
                state = i[3]
                mpiece = white.index(i)
                print(state)
def move(x):
    global notation
    notation = [int(i) for i in x]
    rule()
    
def po(x,y):      #po is the def for position in chessboard, returns piece or blank
    for i in cb:
        if i[1] == x and i[2] == y:
            return i[0]
    return '   '
def chessboard():
    print(po(1,8),po(2,8),po(3,8),po(4,8),po(5,8),po(6,8),po(7,8),po(8,8))
    print(po(1,7),po(2,7),po(3,7),po(4,7),po(5,7),po(6,7),po(7,7),po(8,7))
    print(po(1,6),po(2,6),po(3,6),po(4,6),po(5,6),po(6,6),po(7,6),po(8,6))
    print(po(1,5),po(2,5),po(3,5),po(4,5),po(5,5),po(6,5),po(7,5),po(8,5))
    print(po(1,4),po(2,4),po(3,4),po(4,4),po(5,4),po(6,4),po(7,4),po(8,4))
    print(po(1,3),po(2,3),po(3,3),po(4,3),po(5,3),po(6,3),po(7,3),po(8,3))
    print(po(1,2),po(2,2),po(3,2),po(4,2),po(5,2),po(6,2),po(7,2),po(8,2))
    print(po(1,1),po(2,1),po(3,1),po(4,1),po(5,1),po(6,1),po(7,1),po(8,1))



