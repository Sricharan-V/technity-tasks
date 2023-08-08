# Chess Dictionary Validator
def isvalidchessboard(**chess):
    num=[1,2,3,4,5,6,7,8]
    letters= ['a','b','c','d','e','f','g','h']
    color= ['w', 'b']
    check= []
    pos=[]
    members= ['king', 'queen', 'pawn','bishop','rook','knight']
    try:
        for val in chess.values():
            check.append(val)
        if check.count('king')>1 or check.count('bqueen')>1 or check.count('wking')>1 or check.count('wquueen')>1:
            print("Check number of kings and queens")
        if check.count('bpawn')>8 or check.count('wpawn')>8:
            print("Check mumber of pawns, both black and white")
        if check.count('brook')>2 or check.count('wrook')>2:
            print("Check mumber of rooks, both black and white")
        if check.count('bknight')>2 or check.count('wknight')>2:
            print("Check mumber of knights, both black and white")
        if check.count('bbishop')>2 or check.count('wbishop')>2:
            print("Check mumber of bishops, both black and white")
      

        for key in chess.keys():

            if (int(key[0]) not in num) or (key[1] not in letters):
                print(f"Not valid position {key} ")
            else:
                print("Position values are correct")
        for value in chess.values():
            if value[0] not in color:
                print("Invalid color of player, must be b or w")
            if value[1:] not in members:
                print(f"Not valid chess piece {value[1:]}")
        
    except:
        print("Setup is correct")
    
    
chess= {'1a': 'brook', '4a': 'bking'}
isvalidchessboard(**chess)