import random
from puzzles import *

class Dice:
    def __init__(self):
        self.face = -1

class Player:
    def __init__(self):
        self.position = 0
        self.movesleft = 0
        self.gems = [0 for x in range(6)]
        self.moved = False

        #redGems = gems[0]
        #blueGems = gems[1]
        #yellowGems = gems[2]
        #orangeGems = gems[3]
        #purpleGems = gems[4]
        #greenGems = gems[5]

class Board:
    def __init__(self):
        self.matrix = [[0 for x in range(14)] for y in range(6)] 
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def print(self):
        for i in self.matrix:
            print(i)
        print()

class gameBoard:
    def __init__(self):
        self.theBoard = Board()
        self.fillGems()

        self.players = []
        self.placePlayers()
        self.updatePlayers()

        self.theDice = Dice()

        self.ubongo = False

        self.time = 60
        self.startTimer = False
        self.turns = 1

        self.aiWinner = False

        self.winner = False

        self.puzzles=[puzzle0,puzzle1,puzzle2,puzzle3,puzzle4,puzzle5,puzzle6,puzzle7,puzzle8,puzzle9,puzzle10]

        self.selectedPuzzle = -1
        self.selectedSet = -1
        self.selectedPiece = -1

    def placePlayers(self):
        Player1 = Player()
        Player2 = Player()
        self.players = [Player1,Player2]

    def fillGems(self):
        ##nunca se genera mas de 12 gemas por color
        for i in range(6):
            for j in range(2,14):
                self.theBoard.matrix[i][j] = i

        for i in range(6):
            for j in range(2,14):
                i1 = random.randint(0,5)
                j1 = random.randint(2,11)

                temp = self.theBoard.matrix[i][j]
                self.theBoard.matrix[i][j]=self.theBoard.matrix[i1][j1]
                self.theBoard.matrix[i1][j1]=temp

    
    def updatePlayers(self):
        for i in range(6):
            for j in range(2):
                self.theBoard.matrix[i][j]=0

        for i in range(2):
            self.theBoard.matrix[self.players[i].position][i]=i+10
    
    def restorePiecesPuzzles(self):
        for i in range(len(self.puzzles)):
            self.puzzles[i].restorePieces()
    
    def restoreTestPuzzles(self):
        for i in range(len(self.puzzles)):
            self.puzzles[i].clearTest()

    ##EVENTS
    def ubongoTrigger(self):
        self.restorePiecesPuzzles()
        self.players[0].movesleft=3
        self.players[1].movesleft=2
        self.ubongo = True
    
    def aiWon(self):
        self.restorePiecesPuzzles()
        self.players[0].movesleft=2
        self.players[1].movesleft=3
        self.aiWinner = True

    def throwDice(self):
        self.theDice.face = random.randint(0,5)
        self.selectedPuzzle = random.randint(0,10)
        self.selectedSet = random.randint(0,5)
        self.startTimer = True
    
    def endRound(self):
        self.startTimer = False
        self.aiWinner = False
        self.ubongo = False
        self.theDice.face = -1
        self.players[0].movesleft=0
        self.players[1].movesleft=0
        self.players[0].moved=False
        self.players[1].moved=False
        self.restorePiecesPuzzles()
        self.restoreTestPuzzles()
        self.turns += 1
        
    def getWinner(self):
        if max(self.players[0].gems) > max(self.players[1].gems):
            self.winner = True
        

    ###MOVING
    def movePlayer(self,player,goal):
        if self.players[player].moved == False:
            if goal > self.players[player].position:
                if goal - self.players[player].position <= self.players[player].movesleft:
                    self.players[player].position = goal
                    self.players[player].moved = True
            
            if goal <= self.players[player].position:
                if self.players[player].position - goal <= self.players[player].movesleft:
                    self.players[player].position = goal
                    self.players[player].moved = True
                    
            if self.players[player].moved:
                self.updatePlayers()
                for i in range(2,14):
                    if self.theBoard.matrix[self.players[player].position][i] != -1:
                        self.players[player].gems[self.theBoard.matrix[self.players[player].position][i]] += 1
                        self.theBoard.matrix[self.players[player].position][i] = -1
                        self.players[player].gems[self.theBoard.matrix[self.players[player].position][i+1]] += 1
                        self.theBoard.matrix[self.players[player].position][i+1] = -1
                        break


    def aiMove(self):
        answer = []
        for i in range(6):
            first  = False
            for j in range(2,14):
                if self.theBoard.matrix[i][j] >= 0:
                    first = True
                    if self.theBoard.matrix[i][j] == self.theBoard.matrix[i][j+1]:
                        if self.players[1].position + self.players[1].movesleft >= i and self.players[1].position - self.players[1].movesleft <= i:
                                answer.append(i)
                if first:
                    i += 1
                    j = 0
                    if i == 6:
                        break

        if len(answer) != 0:
            moveTo = random.randint(0,len(answer)-1)
            moveTo = answer[moveTo]
        else:
            moveTo = random.randint(0,self.players[1].movesleft)
        self.movePlayer(1,moveTo)
            
