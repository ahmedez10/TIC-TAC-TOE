import random
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
currentplayer="x"
winner=None
gameRunning=True
def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8]) 
# take player input
def playerinput(board):
    inp=int(input("enter a number  1-9:  "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=currentplayer
    else:
        print("oops player is already in that spot!")

#chaek for win or tie
def chaekhorizontle(board):
    global winner
    if board[0]==board==[1]==board[2]and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5]and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8]and board[6]!="-":
        winner=board[6]
        return True

def  checkrow(board):
    global winner
    if board[0]==board==[3]==board[6]and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7]and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8]and board[2]!="-":
        winner=board[2]
        return True
    
def checkdiag(board):
     global winner
     if board[0]==board==[4]==board[8]and board[0]!="-":
        winner=board[0]
        return True
     elif board[2]==board[4]==board[6]and board[2]!="-":
        winner=board[2]
        return True
def checktie(board):
    global gameRunning
    if "-" not in board:
        printBoard()     
        print("it is a tie")
        gameRunning=False

def checkwin(board):
    if checkdiag(board) or chaekhorizontle(board) or checkrow(board):
        print(f"the winner is {winner}")




# switch the player
def switchplayer():
       global currentplayer
       if currentplayer=="x":
        currentplayer="o"
       else:
        currentplayer="x"

#compuetre        
def computer(board):
    while currentplayer =="o":
        position =random. randint(0,8)
        if board[position]=="-":
            board[position]="o"
            switchplayer()
    


while gameRunning:
    printBoard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    switchplayer() 
    computer(board)
    checkwin(board)
    checktie(board)


