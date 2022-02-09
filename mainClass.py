###############################################################################################################################################################################################################################
# Author Name:      Hunar,Sreelekha and Vinithra
# Date:             06/13/2021
# Program Name:     TicTacToe
# Program Title:    The TicTacToe 5*5 matrix.
# Code flow:        1) startGame() --> __init__() --> printBoard() --> whoGoesFirst() --> playerMove() / compMove() --> checkForWin() --> WriteFile()
#                   2) playerMove() --> fillBoardpositionSpot () --> spaceIsFree() --> printBoard() --> writeLog() --> checkForDraw() / checkForWin() --> write_log2()
#                   3) compMove() --> validateMinimax() --> checkWhoWon() / checkDraw () --> fillBoardpositionSpot () --> spaceIsFree() --> printBoard() --> writeLog() --> checkForDraw() / checkForWin() --> write_log2()
#
# Code description: Main class TicTacToe will invoke the class "startGame()" which has multiple defined functions 
#                   to perform the required game activity. We have two players, user/player will compete against the AI machine ‘computer’. 
#                   The first defined function ‘__init__’ which will print the welcome message to the user followed by printing the tictactoe board positions 
#                   of 5*5 matrix. Code will allow the selection of first player by calling function ‘whoGoesFirst’ which will be done by using predefined 
#                   method randint() which returns an integer value either 0 or 1. If the returned value is 0 then the first move will be made by computer 
#                   else the first move will be done by human player. 
#	                Player is assigned as ‘O’ , computer as ‘X’, X_win, O_win, tie variables are assigned as False; 
#                   gameInProcess variable to True which will run the while loop until we have a winner or the game is a tie
#               	
#                   If the selected turn is ‘player’ then the while condition invokes the method playerMove() followed by compMove() function 
#                   else if it’s the ‘computer’ turn it will invoke compMove() method followed by playerMove() method, and finally checkForWin() function will get 
#                   invoked to verify if we have filled up the available spots according the defined conditions for win, 
#                   if none of the condition is satisfied then while loop will keep running until we have a win or draw situation.
#
#	                The playerMove() function will ask for the player input, if the entered position is between 1-25, it will save the entered number
#                   to the variable “positionSpot” and will make a call to fillBoardpositionSpot() function which will check if the entered position is available 
#                   or not by calling spaceIsFree() function.
#
#	                The compMove() method has two variables bestScore which is set to the minimum value of -2500 and bestMove variable will
#                   store the best value selected by validateMinimax() function.
# 
#                   validateMinimax() method has following parameters: Board, depth, False whose main purpose is to validate the best score
#                   Few conditions are verified if the player or Computer has won or it is a tie situation
#                   Minimax method will recursively iterate the 5*5 board matrix to find the best available spot for the computer move by 
#                   assigning the highest value of 2500 for itself and providing the lowest value to its opponent of -2500.
#
#                   fillBoardpositionSpot() method will take two parameters selectedNumber and positionsSpot
#                   This will verify if the selected spot by the player is available in the 5*5 matrix by calling spaceIsFree() method
#                   If the spot is avaliable then it will save the selectedNumber in the matrix, else it will throw an error message to the player
#                   stating the spot is unavailable
#                   Also, it will invoke the log.write() method which will write the entry of player in the log file to save of all the moves 
#                   happening during the game
#                   Further, it will invoke checkDraw() and checkForWin () methods to validate if anybody won the game or if its a tie
#                   Parallely each entry will get write to the log file by calling write_log2 function
#   
#                   spaceIsFree() function will match the value entered by player 
# 
#                   checkforwin() method has defined Win conditions and if one of them gets satisfied then the function basically returns True
#                   else False. 
# 
#                   checkWhoWin() method takes in player_pos as parameter and will validate who's player positionSpot has got the Win condition
#                   satisfied.
# 
#                   checkDraw() method will verify all the available spots of 5*5 matrix are occupied once we have false condition from checkWhoWin() method
#                   
#                   write_log() and write_log2() methods will write each move played by the players till the game ends.
#
#                   tictactoe.txt file gets created as the ouput of this program.
# References -     geeksforgeeks. (2021). Minimax Algorithm in Game Theory | Set 3 (Tic-Tac-Toe AI – Finding optimal move). https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
#                  Somani, S. (2020). Tic-Tac-Toe Game In Python. Sharpcorner. https://www.c-sharpcorner.com/UploadFile/75a48f/tic-tac-toe-game-in-python/
#                  Tic-Tac-Toe with the Minimax Algorithm. (2019, June 15). Nestedsoftware.com. https://nestedsoftware.com/2019/06/15/tic-tac-toe-with-the-minimax-algorithm-5988.123625.html
#                  Von Neumann’s Minimax Theorem/ algorithm. (2018, July 22). OpenGenus IQ: Computing Expertise & Legacy. https://iq.opengenus.org/minimax-theorem-algorithm-von-neumann/
###############################################################################################################################################################################################################################

import TicTacToe

if __name__ == '__main__':
    # Initiate the class to kick start the game!    
    TicTacToe.startGame()
