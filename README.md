# Chess
Chess program for EPQ
The programme is aiming to develop a full functioning program which allows Player V Player and Player V AI
# Type of board representation
- The first edition was represented by a 8*8 array
- The second edition was represented in piece list
## Features
- Every piece in chess is assigned a variable name of it's name, for example, black side pawn 1 would be named as 'bp1' etc
- The variable for each piece is a list contains 4 element, which are [piece name(string) , position on x axis(intiger) , position on y axis(intiger) , chess type (intiger)]
    - Willing to change to 5 elements which the 5th element will be the unicode chess thimble.(Not acchieved yet)
- Piece name is used to define every piece's identity, and trace where it is on the chessboard
- position on x axis and y axis is used to locate it's location on the chessboard. Every Position's state can be found bby function po(x,y,s), x and y are coordinates, and s is the type: 0 for name, 1 for x axis, 2 for y axis, and 3 for type of piece.
- Rules are written in functions, when input intendent to move a piece, program will select which rule to apply due to which type of piece it is.
- The chessboard doesn't quite exist, where every chess manage it's own position. This is easier to achieve when representing the pieces, but harder to make moves  because every piece is independent, where if the move to be made, a skan to all pieces is required.
Also overlapping moves will not call an error so a function of avoiding overlapping is required.
 - Moves made are represented by a 4 digit number, where the first two digits are the notation where they are from, and the last two are where they are to go. The move function will generate all possibilities of moving piece, and store it in a list named "possibles", and the move that player is willing to go is checked if the move is in the list "possibilities", and if in, it's a legal omve, but if isn't, it's illigal and player will be asked to re-check their move.



## Functions
- chessboard():   Print the current chessboard. (Warning: chessboard() function is based on po and list cb, for best outcome and avoiding that the cb list haven't updates after a move, use fresh() to update changes.
- move(4 digit intiger):   the move() function allows the player to make the move of piece, the first two digit is to define which piece the player intended to move, and the second two digit is to state where the player to move the piece to. All positions are written in (x,y)
- test(): test() function is used as a debugging (cheating) tool, it can move which ever piece to whereever it could possibly be, ignoring the rules. To do this, simply redefine the piece's list and change the position. This function always end with fresh() and chessboard() to make sure the cb and chessboard are updated.


## Pieces Rules
### Knight
- There is only maximum 8 possible movements a knight can possibly acchieve, so exhaustion should be able to achieve it with least time.
- Is it possible like all rules are layed out, that a knight's rule ca be componded into a function, and at every possibility, it calls that function to check if it's a legal move, because every checing is homogenised.

## Current progress
- The program has been built up to queen's rule, 
- (ALL FINISHED)there is black pawn's rule, knight's rule and king's rule to be finished. 
- Takeover piece has been developed, but the piece that has been eaten is only change it's variable to [None,0,0,None], it still have position of (0,0), it is reasonable to fear it might interupt with rules and causing unexpected problem. 
- Round swaping and check mating is awaited to be done as well.
- UPDATE 6-4-2017:      Finished king and knight rules
- UPDATE 6-4-2017:      Fixing an error with spelling
- UPDATE 10-4-2017:     Fixing an error with when king or queen are taken over, their [0] is 'bk ' with space but their variable name doesn't have the variable name.
- UPDATE 10-4-2017:     Game now can finish when either side of king is taken.
- UPDATE 10-4-2017:     Added list 'record', that record every movement made my 'move(4digit movement)', it's executable by execrecord[?]
- UPDATE 11-4-2017：    Chess playing program is tested briefly proving it works, now aiming for AI playing chess.
- UPDATE 21-4-2017:     Now there is AI can be used to play with,but only low level AI, no overlooking for future moves.



#Bibliography
 - https://chessprogramming.wikispaces.com/Piece-Lists (Idea of defining every chess on the board as arrays, and occupies them)
    -Piece-Lists are lists or arrays of all up to 32 pieces (including pawns and king) on the board. Likely, type and color of pieces are associated by a certain index range or disjoint lists or arrays. Each element of the list or array for each particular piece associates the square occupied by this piece. 
 - http://chessprogramming.wikispaces.com/General+Setwise+Operations 
 - https://github.com/niklasf/python-chess/blob/master/chess/__init__.py
 - https://docs.python.org/2/howto/unicode.html
 - https://chessprogramming.wikispaces.com/Board+Representation
 - http://www.stmintz.com/ccc/index.php?id=70162 (Represent board by an array, value represent pieces)
 - http://www.stmintz.com/ccc/index.php?id=70116 (Used array of (10*10))
     -could be another way of representing board. Firstly tried, but failed.
 - http://www.stmintz.com/ccc/index.php?id=70235 (Using the idea of directions instead of pure number adddings and minusing)
     - if directions can be used, it can save a lot of code by classifing each moves, and won't have to write them every time.
 
