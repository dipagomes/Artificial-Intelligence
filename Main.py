board = {
    1:' ', 2:' ', 3:' ',
    4:' ', 5:' ', 6:' ',    #initialized the board as every position is empty
    7:' ', 8:' ', 9:' '
}


def printBoard(board):
    print(board[1]+ '|' + board[2]+ '|'+ board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5]+ '|'+ board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8]+ '|'+ board[9])
    print("\n")

printBoard(board)

def spaceFree(position):
    if(board[position]==' '):  #if the position is empty ...Acyually checking for the empty position
        return True
    else:
        return False    

def checkDraw():
   for key in board.keys():
    if board[key] == ' ':
        return False        #Returning false if there is still empty places we will play otherwise returns false that means draw

   return True  

def checkWinning():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != mark):
        return True
    else:
        return False


def insertLetter(letter,position):
    if spaceFree(position):
        board[position] = letter
        printBoard(board)
        if(checkDraw()):
           print("Draw!!")
           print()
           exit() 
        
        if checkWinning():
            if letter == 'X':
               print("Computer Wins!!Congratulations...")
               print()
               exit()

            else:
                print("Player Wins!!Congratulations...")
                print() 
                exit()
        return

    else:
        print("Can't Insert there!!")
        position = int(input("Enter a new position: "))
        insertLetter(letter,position)
        return


player = '0'
computer = 'X'
def playerMove():
    position = float(input("Enter the position for 'Player': "))
    insertLetter(player,position)
    return

def computerMove():
    bestScore = -1000   #just intialized
    bestMove = 0

    for key in board.keys():
        if(board[key]==' '):
            board[key] = computer
            score = minimax(board,0,False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    
    insertLetter(computer,bestMove)
    return



def minimax(board,depth,isMaximizing):
    if checkWhichMarkWon(computer):
        return 1
    
    elif checkWhichMarkWon(player):
        return -1

    elif checkDraw():
        return 0

    if isMaximizing:

        bestScore = -1000   #just intialized
     

        for key in board.keys():
            if(board[key]==' '):
                board[key] = computer
                score = minimax(board,0,False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800   #just intialized
  

        for key in board.keys():
            if(board[key]==' '):
                board[key] = computer
                score = minimax(board,0,True)    #enemy
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        
        return bestScore
               



while not checkWinning():
    computerMove()
    playerMove()