import time
import random
import math
from properties import gameTick, width, height
half = math.floor(width/2)




#Define tetrino/block
class tetrino:
    def __init__(self, blockChoice):
        #reset all block positions to starting positions
        line = [[0,half], [1,half], [2,half], [3,half]]
        square = [[0,half], [1,half], [0,half+1], [1,half+1]]
        skew = [[0,half], [0,half+1], [1,half+1], [1,half+2]]
        invSkew = [[1,half], [1,half+1], [0,half+1], [0,half+2]]
        Tblock = [[0,half+1], [1,half], [1,half+1], [1,half+2]]
        Lblock = [[0,half], [1,half], [1,half+1], [1,half+2]]
        invL =  [[1,half], [1,half+1],[1,half+2], [0,half+2]]

        #add all positions to a dictionary
        blockCoords = {'line':line, 'square':square, 'skew':skew,
        'invSkew':invSkew, 'Tblock':Tblock, 'Lblock':Lblock ,'invL':invL}

        #if the block choice is random generate, choose a random block
        if(blockChoice =='rand'):
            blockChoice = random.choice(list(blockCoords))
        self.name = blockChoice
        #assign blocks coordinates to tetrino coordinates
        self.coords = list(blockCoords[blockChoice])
