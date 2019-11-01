from keyboard_master import keyboard
import gameBoard
import random
import time
from properties import gameTick, width, height
def printCenter(text):
    print(" "*int(width/2-4)+text+" "*int(width/2-4))




playagain = True

#Generate emmpty game board
gameBoard = gameBoard.gameBoard()
while(playagain):
    #Loop while escape key isnt pressed
    gameBoard.updateBoard(0,4,False)
    while(not(keyboard.is_pressed('escape')) and not gameBoard.checkGameOver()):
        #if a key is pressed update board and move corresponding block
        if(keyboard.is_pressed('left')):
            gameBoard.updateBoard(-1,0,False)
        elif(keyboard.is_pressed('right')):
            gameBoard.updateBoard(1,0,False)
        elif(keyboard.is_pressed('down')):
            gameBoard.updateBoard(0,2,False)
        elif(keyboard.is_pressed('space')):
            gameBoard.updateBoard(0,6,False)
        elif(keyboard.is_pressed('up')):
            gameBoard.updateBoard(0,0,True)
        elif(keyboard.is_pressed('c')):
            gameBoard.holdTetrino()
        #if no key is pressed move block down 1
        else:
            gameBoard.updateBoard(0,1,False)

        #wait .5s before updating
        time.sleep(gameTick)

    #Game Finished
    for i in range(4):
        print()
    printCenter("GAMEOVER")

    ans=""
    while(not ans=='Y' and not ans =='N'):
        ans = input("Play Again(Y/N): ")
        if(ans == "Y"):
            playagain = True
            gameBoard.reset()
        elif(ans == "N"):
            playagain = False
