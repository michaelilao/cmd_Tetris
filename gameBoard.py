import time
import random
import math
import tetrinos
from properties import gameTick, width, height
half = math.floor(width/2)


#create a game board where actions will update
class gameBoard:
    def __init__(self):
        #Create an empty Board
        self.score = 0
        self.board = []
        self.currentTetrino = ''
        #add a starting tetrino
        self.addTetrino('rand')
        #Create a 2D array of size 12x18
        for i in range(height):
            #add num height empty arrays
            self.board.append([])
            for j in range(width):
                #loop through each empy array and add num width keys
                #Sides and Bottom assigned wall key (3)
                if(i==(height-1) or j==0 or j==(width-1)):
                    self.board[i].append(3)
                #else assigned empty key (0)
                else:
                    self.board[i].append(0)

    def reset(self):
        self.score = 0
        self.board = []
        self.currentTetrino = ''
        self.holdingTetrini = ''
        #add a starting tetrino
        self.addTetrino('rand')
        #Create a 2D array of size 12x18
        for i in range(height):
            #add num height empty arrays
            self.board.append([])
            for j in range(width):
                #loop through each empy array and add num width keys
                #Sides and Bottom assigned wall key (3)
                if(i==(height-1) or j==0 or j==(width-1)):
                    self.board[i].append(3)
                #else assigned empty key (0)
                else:
                    self.board[i].append(0)


    #Updates the board whenever action is pressed
    def updateBoard(self,xMovement,yMovment,doRotate):
        #if the next move does not cause tetrino to stop moving, update tetrino
        if(not self.checkStopped()):
            #get coordinates of current position and position to move to

            coords = self.moveBlock(xMovement,yMovment,doRotate)
            oldCoords = coords[0]
            newCoords = coords[1]
                #loop through current position and change to empty key(0)
            for i in range(4):
                self.setCoords(oldCoords[i][1], oldCoords[i][0], 0)
                #loop through new position and change to falling key(2)
            for i in range(4):
                self.setCoords(newCoords[i][1], newCoords[i][0], 2)
        #if block does stop gen new tetrino
        else:
            self.addTetrino('rand')

        #Check if there are any full lines
        self.checkClearLine()
        #print the updated board
        self.printBoard()

    def checkGameOver(self):
        for i in self.board[1]:
            if(i==4):
                return True
        return False

    #check if there are any lines to clear
    def checkClearLine(self):
        #loop through board array and check if there are any full lines
        #a full line would have all indexs key(4), but 2 (wall keys)
        linesCleared = []
        for i in range(height):
            if(self.board[i].count(4)==(len(self.board[i]))-2):
                #if a full line is found, update all non wall keys to 0
                for j in range(1,width-1):
                    self.setCoords(j,i,0)
                self.printBoard()
                linesCleared.append(i)
        #loop through the lines that have been cleared
        for i in linesCleared:
            #starting with lowest line. move all rows down one
            for j in reversed(range(i)):
                self.board[j+1] = self.board[j].copy()
        self.updateScore(len(linesCleared))


    def updateScore(self,numLines):
        if(numLines == 1):
            self.score += 40
        if(numLines == 2):
            self.score += 100
        if(numLines == 3):
            self.score += 400
        if(numLines == 4):
            self.score += 1200
    #Moving tetrino


    def moveBlock(self, xMove, yMove,doRotate):
        oldCoords = []
        newCoords = []
        collisionDetected = False
        #add curent tetrinos coordinates to array
        for i in range(4):
            y = self.currentTetrino.coords[i][0]
            x = self.currentTetrino.coords[i][1]
            oldCoords.append([y,x])
        ox = self.currentTetrino.coords[0][1]
        oy = self.currentTetrino.coords[0][0]
        #add proposed tetrino coordinates to array
        for i in range(4):
            if(doRotate):
                x, y = self.rotateBlock(ox,oy, self.currentTetrino.coords[i][1] ,self.currentTetrino.coords[i][0], math.radians(90))
            else:
                y = self.currentTetrino.coords[i][0]+yMove
                x = self.currentTetrino.coords[i][1]+xMove
            newCoords.append([y,x])
            #if any of these coordinates would move into a stagnant or wall key then
            #return the oldCoords for oldCoords and newCoords to stop move
            if(self.board[y][x] == 4 or self.board[y][x] == 3):
                return [oldCoords, oldCoords]
        #Update current tetrinos new coordinates
        self.currentTetrino.coords = newCoords
        return [oldCoords, newCoords]




    def addTetrino(self,choice):
        #Generate random tetrino and assign it to current tetrino
        self.currentTetrino = tetrinos.tetrino(choice)


    #check if block will hit floor or another stagnant tetrino
    def checkStopped(self):
        #loop through tetrinos coordinates
        for i in range(4):
            y = self.currentTetrino.coords[i][0]
            x = self.currentTetrino.coords[i][1]
            #if the coordinates hit the floor or
            #they collide into a stagnant key
            if(y==height-2 or self.board[y+1][x]==4):
                #Set Tetrino to stagnant (4)
                for j in range(4):
                    y = self.currentTetrino.coords[j][0]
                    x = self.currentTetrino.coords[j][1]
                    self.setCoords(x,y,4)
                #collided with something
                return True
        #didnt collide
        return False

    def rotateBlock(self,ox,oy, px,py, angle):


        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return int(qx), int(qy)


    #Set on the board array a value at x,y
    def setCoords(self,x,y,value):
        self.board[y][x] = value

    #print board on cmd
    def printBoard(self):
        ##loop through board array
        #first two rows are hidden as game will end when first shown row is hit
        for i in range(2,height):
            if(i!=0):
                print()
            for j in range(width):
                #print a key according to numerical value
                if( self.board[i][j]==4):
                    print("#", end = '')
                if(self.board[i][j]==3):
                    print("*", end = '')
                if(self.board[i][j]==2):
                    print("X", end = '')
                if(self.board[i][j]<=1):
                    print(" ", end = '')
            print(i, end='')
            if(i == 4):
                #print score on line 4
                print("\tScore:",self.score, end='')
        print()
