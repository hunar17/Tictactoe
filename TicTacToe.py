import random
import os

class startGame:

    def __init__(self):
        #Welcome message to a user 
        print('-------------Welcome to Tic-Tac-Toe--------------')
        print("\n")

        #Created a board array to create the spots
        self.board = {1: ' ',   2: ' ', 3: ' ',   4: ' ', 5: ' ',
                      6: ' ',   7: ' ', 8: ' ',   9: ' ', 10: ' ',
                      11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
                      16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
                      21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' '}

        self.printBoard(self.board)
        #Print the board positions of tictactoe 5*5 matrix
        print("Board positions are as follow:")
        print("1,  2,  3,  4,  5 ")
        print("6,  7,  8,  9,  10 ")
        print("11, 12, 13, 14, 15 ")
        print("16, 17, 18, 19, 20 ")
        print("21, 22, 23, 24, 25 ")
        print("\n")
        # Lets make a choice who will play first
        print("Lets make random choice who will make first turn")
        self.turn = self.whoGoesFirst()
        print('The ' + self.turn + ' will go first.')
        #Assigning the two variables 'player' and 'computer'
        self.player = 'O'
        self.computer = 'X'
        #Assigning variables to capture who wins or does match gets draw
        self.X_win = False
        self.O_win = False
        self.tie = False
        # Declaring 'gameInProcess' variable to True which will run the while loop
        # until the condition becomes false
        gameInProcess = True
        # if the file 'tictactoe.txt' exists it will remove the existing file
        if (os.path.isfile('tictactoe.txt')):    
            os.remove('tictactoe.txt')
        #Write the first comment to the log file
        self.log = open('tictactoe.txt', 'a')
        while gameInProcess:
            if self.turn == 'player':
                self.playerMove()
                self.compMove()
            else:
                self.compMove()
                self.playerMove()
            # CheckForWin function will validate the selected entry and will save the spot
            self.checkForWin()

    #The below function will display the board array spots
    def printBoard(self, board):
        print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5])
        print('-+-+-+-+-')
        print(board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10])
        print('-+-+-+-+-')
        print(board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14] + '|' + board[15])
        print('-+-+-+-+-')
        print(board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20])
        print('-+-+-+-+-')
        print(board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25])
        print("\n")

    #The below function will check which positionSpot is available
    def spaceIsFree(self, positionSpot):
        if self.board[positionSpot] == ' ':
            return True
        else:
            return False

    #The fillBoardpositionSpot function will save the selected Number to the board array after
    # validating the positionSpot is available or not. 
    # If user will try to enter to the occupied positionSpot, it will perform a valid test 
    # and will throw an error message
    # It will also check if it is draw or who has won the game.
    def fillBoardpositionSpot(self, selectedNumber, positionSpot):
        self.X_win, self.O_win, self.tie
        if self.spaceIsFree(positionSpot):
            #Write the current positionSpot of computer to the log file
            log = open('tictactoe.txt', 'a')
            if selectedNumber == 'O':
                log.write("positionSpot entered by Player 'O' is: "+ format(int(positionSpot)) + "\n")
                log.seek(0)
            else:
                log.write("positionSpot entered by Computer 'X' is: "+ format(int(positionSpot)) + "\n")
                log.seek(0)
            self.board[positionSpot] = selectedNumber
            self.printBoard(self.board)
            self.write_log()
            if (self.checkDraw()):
                print("Draw!")
                self.write_log2()
                gameInProcess = False
                exit()
            if self.checkForWin():
                if selectedNumber == 'X':
                    print("Oops you lost! Try again!")
                    self.O_win = True
                    self.write_log2()
                    gameInProcess = False
                    exit()
                else:
                    print("Hurray, you Won!")
                    self.X_win = True
                    self.write_log2()
                    gameInProcess = False
                    exit()
            return

        else:
            print("Can't insert there!")
            positionSpot = int(input("Please enter new positionSpot:  "))
            self.fillBoardpositionSpot(selectedNumber, positionSpot)
            return

	# Checkforwin function will validate all the possible matches to declare the final win
    def checkForWin(self):
		#Horizontal section
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == self.board[4] and self.board[1] != ' '): return True
        elif (self.board[2] == self.board[3] and self.board[2] == self.board[4] and self.board[2] == self.board[5] and self.board[2] != ' '): return True
        elif (self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[6] == self.board[9] and self.board[6] != ' '): return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == self.board[10] and self.board[7] != ' '): return True
        elif (self.board[11] == self.board[12] and self.board[11] == self.board[13] and self.board[11] == self.board[14] and self.board[11] != ' '): return True
        elif (self.board[12] == self.board[13] and self.board[12] == self.board[14] and self.board[12] == self.board[15] and self.board[12] != ' '): return True
        elif (self.board[16] == self.board[17] and self.board[16] == self.board[18] and self.board[16] == self.board[19] and self.board[16] != ' '): return True
        elif (self.board[17] == self.board[18] and self.board[17] == self.board[19] and self.board[17] == self.board[20] and self.board[17] != ' '): return True
        elif (self.board[21] == self.board[22] and self.board[21] == self.board[23] and self.board[21] == self.board[24] and self.board[21] != ' '): return True
        elif (self.board[22] == self.board[23] and self.board[22] == self.board[24] and self.board[22] == self.board[25] and self.board[22] != ' '): return True
        		
		    #vertical section
        elif (self.board[1] == self.board[6] and self.board[1] == self.board[11] and self.board[1] == self.board[16] and self.board[1] != ' '):	return True
        elif (self.board[6] == self.board[11] and self.board[6] == self.board[16] and self.board[6] == self.board[21] and self.board[6] != ' '): return True
        elif (self.board[2] == self.board[7] and self.board[2] == self.board[12] and self.board[2] == self.board[17] and self.board[2] != ' '): return True
        elif (self.board[7] == self.board[12] and self.board[7] == self.board[17] and self.board[7] == self.board[22] and self.board[7] != ' '): return True
        elif (self.board[3] == self.board[8] and self.board[3] == self.board[13] and self.board[3] == self.board[18] and self.board[3] != ' '): return True
        elif (self.board[8] == self.board[13] and self.board[8] == self.board[18] and self.board[8] == self.board[23] and self.board[8] != ' '): return True
        elif (self.board[4] == self.board[9] and self.board[4] == self.board[14] and self.board[4] == self.board[19] and self.board[4] != ' '): return True
        elif (self.board[9] == self.board[14] and self.board[9] == self.board[19] and self.board[9] == self.board[24] and self.board[9] != ' '): return True
        elif (self.board[5] == self.board[10] and self.board[5] == self.board[15] and self.board[5] == self.board[20] and self.board[5] != ' '): return True
        elif (self.board[10] == self.board[15] and self.board[10] == self.board[20] and self.board[10] == self.board[25] and self.board[10] != ' '): return True
        
		    #Left Diagonal section
        elif (self.board[1] == self.board[7] and self.board[1] == self.board[13] and self.board[1] == self.board[19] and self.board[1] != ' '): return True 
        elif (self.board[7] == self.board[13] and self.board[7] == self.board[19] and self.board[7] == self.board[25] and self.board[7] != ' '): return True
        elif (self.board[6] == self.board[12] and self.board[6] == self.board[18] and self.board[6] == self.board[24] and self.board[6] != ' '): return True
        elif (self.board[2] == self.board[8] and self.board[2] == self.board[14] and self.board[2] == self.board[20] and self.board[2] != ' '): return True
        #Right Diagnal checking    
        elif (self.board[5] == self.board[9] and self.board[5] == self.board[13] and self.board[5] == self.board[17] and self.board[5] != ' '): return True
        elif (self.board[9] == self.board[13] and self.board[9] == self.board[17] and self.board[9] == self.board[21] and self.board[9] != ' '): return True
        elif (self.board[10] == self.board[14] and self.board[10] == self.board[18] and self.board[10] == self.board[22] and self.board[10] != ' '): return True
        elif (self.board[4] == self.board[8] and self.board[4] == self.board[12] and self.board[4] == self.board[16] and self.board[4] != ' '): return True
        else:
            return False
           
    # The below function will validate which player's positionSpot has won, is it the player's positionSpot
    # or Computer's player_pos who has made the first win 
    def checkWhoWon(self, player_pos):

        #Horizontal section
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == self.board[4] and self.board[1] == player_pos):
            return True
        elif (self.board[2] == self.board[3] and self.board[2] == self.board[4] and self.board[2] == self.board[5] and self.board[2] == player_pos):
            return True
        elif (self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[6] == self.board[9] and self.board[6] == player_pos):
            return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == self.board[10] and self.board[7] == player_pos):
            return True
        elif (self.board[11] == self.board[12] and self.board[11] == self.board[13] and self.board[11] == self.board[14] and self.board[11] == player_pos):
            return True
        elif (self.board[12] == self.board[13] and self.board[12] == self.board[14] and self.board[12] == self.board[15] and self.board[12] == player_pos):
            return True
        elif (self.board[16] == self.board[17] and self.board[16] == self.board[18] and self.board[16] == self.board[19] and self.board[16] == player_pos):
            return True
        elif (self.board[17] == self.board[18] and self.board[17] == self.board[19] and self.board[17] == self.board[20] and self.board[17] == player_pos):
            return True
        elif (self.board[21] == self.board[22] and self.board[21] == self.board[23] and self.board[21] == self.board[24] and self.board[21] == player_pos):
            return True
        elif (self.board[22] == self.board[23] and self.board[22] == self.board[24] and self.board[22] == self.board[25] and self.board[22] == player_pos):
            return True
            
        #vertical section
        elif (self.board[1] == self.board[6] and self.board[1] == self.board[11] and self.board[1] == self.board[16] and self.board[1] == player_pos):
            return True
        elif (self.board[6] == self.board[11] and self.board[6] == self.board[16] and self.board[6] == self.board[21] and self.board[6] == player_pos):
            return True
        elif (self.board[2] == self.board[7] and self.board[2] == self.board[12] and self.board[2] == self.board[17] and self.board[2] == player_pos):
            return True
        elif (self.board[7] == self.board[12] and self.board[7] == self.board[17] and self.board[7] == self.board[22] and self.board[7] == player_pos):
            return True
        elif (self.board[3] == self.board[8] and self.board[3] == self.board[13] and self.board[3] == self.board[18] and self.board[3] == player_pos):
            return True
        elif (self.board[8] == self.board[13] and self.board[8] == self.board[18] and self.board[8] == self.board[23] and self.board[8] == player_pos):
            return True
        elif (self.board[4] == self.board[9] and self.board[4] == self.board[14] and self.board[4] == self.board[19] and self.board[4] == player_pos):
            return True
        elif (self.board[9] == self.board[14] and self.board[9] == self.board[19] and self.board[9] == self.board[24] and self.board[9] == player_pos):
            return True
        elif (self.board[5] == self.board[10] and self.board[5] == self.board[15] and self.board[5] == self.board[20] and self.board[5] == player_pos):
            return True
        elif (self.board[10] == self.board[15] and self.board[10] == self.board[20] and self.board[10] == self.board[25] and self.board[10] == player_pos):
            return True
     
        #Left Diagonal section
        elif (self.board[1] == self.board[7] and self.board[1] == self.board[13] and self.board[1] == self.board[19] and self.board[1] == player_pos):
            return True
        elif (self.board[7] == self.board[13] and self.board[7] == self.board[19] and self.board[7] == self.board[25] and self.board[7] == player_pos):
            return True
        elif (self.board[6] == self.board[12] and self.board[6] == self.board[18] and self.board[6] == self.board[24] and self.board[6] == player_pos):
                return True
        elif (self.board[2] == self.board[8] and self.board[2] == self.board[14] and self.board[2] == self.board[20] and self.board[2] == player_pos):
            return True        
        #Right Diagnal checking    
        elif (self.board[5] == self.board[9] and self.board[5] == self.board[13] and self.board[5] == self.board[17] and self.board[5] == player_pos):
            return True
        elif (self.board[9] == self.board[13] and self.board[9] == self.board[17] and self.board[9] == self.board[21] and self.board[9] == player_pos):
            return True
        elif (self.board[10] == self.board[14] and self.board[10] == self.board[18] and self.board[10] == self.board[22] and self.board[10] == player_pos):
            return True
        elif (self.board[4] == self.board[8] and self.board[4] == self.board[12] and self.board[4] == self.board[16] and self.board[4] == player_pos):
            return True        
        else:
            return False

    # The below function will verify if all the positionSpots have been marked and it will return true 
    # else it will return false, if all the positionSpots in the array has not been utilized yet.
    def checkDraw(self):
        for key in self.board.keys():
            if (self.board[key] == ' '):
                return False
        return True

    # The playerMove function will ask for the player input positionSpot and will save it
    def playerMove(self):
        if self.O_win:
            return
        positionSpot = int(input("Enter the positionSpot between 1-25 for 'O':  "))
        try:
            while (positionSpot < 1 or positionSpot > 25):
                positionSpot = int(input("Please enter positionSpot between 1-25: "))
        except ValueError:
            print("Oops! That is an invalid input. Please try again and enter valid positionSpot from 1-25. ")
        else:
            print("The positionSpot entered by O is: ",positionSpot)
            self.fillBoardpositionSpot(self.player, positionSpot)
        return

    # The compMove function will select a positionSpot based on a random positionSpot and
    # It will also call 'validateMinimax' function which will select the optimal move for AI 
    # so that its oponent 'player' can loose the game
    def compMove(self):
        if self.X_win:
            return
        bestScore = -2500
        bestMove = 0
        for key in self.board.keys():
            if (self.board[key] == ' '):
                self.board[key] = self.computer
                score = self.validateMinimax(self.board, 0, False)
                self.board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key

        print("The positionSpot selected by Computer is: ",bestMove )
        self.fillBoardpositionSpot(self.computer, bestMove)
        return

    # The below function will write each move to the log file 'tictactoe.txt'
    def write_log(self):
        log = open('tictactoe.txt', 'a')
        log.seek(0)
        log.write("\n\n {} | {} | {} | {} | {} \n ------------------ \n {} | {} | {} | {} | {} \n ------------------ \
        \n {} | {} | {} | {} | {} \n ------------------ \n {} | {} | {} | {} | {} \n ------------------ \n {} | {} | {} | {} | {} \n\n"\
        .format(self.board[1],self.board[2],self.board[3],self.board[4],self.board[5],self.board[6],self.board[7],self.board[8],\
        self.board[9],self.board[10],self.board[11],self.board[12],self.board[13],self.board[14],self.board[15],self.board[16],self.board[17],\
        self.board[18],self.board[19],self.board[20],self.board[21],self.board[22],self.board[23],self.board[24],self.board[25]))
        log.seek(0)

    # The below function will write the final winner
    def write_log2(self):
        log = open('tictactoe.txt', 'a')
        if self.X_win:
            log.write('Congrats, you won the game :) \n ')
            log.seek(0)
        elif self.O_win:
            log.write('Oops, you lost :( \n ')
            log.seek(0)
        else:
            log.write('It is a tie \n')
            log.seek(0)
        log.close()

    # The validateMinimax algorithim will validate the best score 
    # score = validateMinimax(board, depth, isMax):
    # board: is the current board in recursion;
    # depth: index of the next state;
    # isMax: if a player is MAX (+1) will be MIN (-1) and vice versa.
    def validateMinimax(self, board, depth, isMax):
        if (self.checkWhoWon(self.computer)):
            return 1
        elif (self.checkWhoWon(self.player)):
            return -1
        elif (self.checkDraw()):
            return 0

        if (isMax):
            bestScore = -2500
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.computer
                    score = self.validateMinimax(board, depth + 1, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 2500
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.player
                    score = self.validateMinimax(board, depth + 1, True)
                    board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore

    #The below function will validate who will play first move
    def whoGoesFirst(self):
        # Randomly choose which player goes first.
        if random.randint(0, 1) == 0:
             return 'computer'
        else:
             return 'player'
  