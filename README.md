# Chess
Chess program for EPQ
The programme is aiming to develop a full functioning program which allows Player V Player and Player V AI
## Features
- Every piece in chess is assigned a variable name of it'sname, for example, black side pawn 1 would be named as 'bp1' etc
- The variable for each piece is a list contains 4 element, which are [piece name(string) , position on x axis(intiger) , position on y axis(intiger) , chess type (intiger)]
- Piece name is used to define every piece's identity, and trace where it is on the chessboard
- position on x axis and y axis is used to locate it's location on the chessboard. Every Position's state can be found bby function po(x,y,s), x and y are coordinates, and s is the type: 0 for name, 1 for x axis, 2 for y axis, and 3 for type of piece.
- Rules are written in functions, when input intendent to move a piece, program will select which rule to apply due to which type of piece it is.


## Functions
- chessboard():   Print the current chessboard. (Warning: chessboard() function is based on po and list cb, for best outcome and avoiding that the cb list haven't updates after a move, use fresh() to update changes.
- move(4 digit intiger):   the move() function allows the player to make the move of piece, the first two digit is to define which piece the player intended to move, and the second two digit is to state where the player to move the piece to. All positions are written in (x,y)
- test(): test() function is used as a debugging (cheating) tool, it can move which ever piece to whereever it could possibly be, ignoring the rules. To do this, simply redefine the piece's list and change the position. This function always end with fresh() and chessboard() to make sure the cb and chessboard are updated.



## Current progress
    The program has been built up to queen's rule, there is only black pawn's rule, knight's rule and king's rule to be finished. Takeover piece has been developed, but the piece that has been eaten is only change it's variable to [None,0,0,None], it still have position of (0,0), it is reasonable to fear it might interupt with rules and casing unexpected problem. Also round swaping and check mating is awaited to be done as well.
    
