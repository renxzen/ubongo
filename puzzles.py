from pieces import *

class Puzzle:
    def __init__(self, matrix):
        self.height = len(matrix)
        self.width = len(matrix[0])

        self.matrix = matrix
        self.solved = deepcopy(self.matrix)
        self.test = deepcopy(self.matrix)

        self.sets = []

    def print(self):
        for h in self.matrix: print(h)
        print()

    def printSolved(self):
        for h in self.solved: print(h)
        print()

    def printTest(self):
        for h in self.test: print(h)
        print()
    
    def restorePieces(self):
        for i in range(len(self.sets)):
            for j in range (len(self.sets[i])):
                self.sets[i][j].restore()
                self.sets[i][j].selected = False
                self.sets[i][j].startRotating = False

    def restoreSolved(self):
        self.solved = deepcopy(self.matrix)

    # Main Algorithm
    def fill(self):
        for i in self.solved:
            for j in i:
                if j == 0:
                    return False
        return True

    def check(self, pu_row, pu_col, pieces, index):
        pu_rows = self.height
        pu_cols = self.width
        pi_rows = pieces[index].height
        pi_cols = pieces[index].width
        pu_col -= pieces[index].start_col()
        if pu_col >= 0 and pu_row+pi_rows-1 < pu_rows and pu_col+pi_cols-1 < pu_cols:
            for i in range(pi_rows):
                for j in range(pi_cols):
                    if pieces[index].matrix[i][j] == 1 and self.solved[pu_row+i][pu_col+j] > 0:
                        return False
            return True
        else:
            return False
    
    def place(self, pu_row, pu_col, pieces, index):
        pi_rows = pieces[index].height
        pi_cols = pieces[index].width
        pu_col -= pieces[index].start_col()
        for i in range(pi_rows):
                for j in range(pi_cols):
                    if pieces[index].matrix[i][j] == 1:
                        self.solved[pu_row+i][pu_col+j] = index+2

    def solving(self, stepback,pieces,index):
        if index == len(pieces):
            if self.fill():
                return True
            else:
                return False
        for i in range(self.height):
            for j in range(self.width):
                if self.solved[i][j]==0:
                    pieces[index].restore()
                    for k in range(8):
                        if k == 4:
                            pieces[index].flip()
                        if self.check(i, j, pieces, index): 
                            stepback = deepcopy(self.solved)
                            self.place(i, j, pieces, index)
                            if self.solving(stepback,pieces, index + 1):
                                return True
                            else:
                                self.solved = deepcopy(stepback)
                        pieces[index].rotate()
        return False

    def ubongo(self, setNumber):
        self.solved = deepcopy(self.matrix)
        stepback = deepcopy(self.matrix)

        self.solving(stepback,self.sets[setNumber],0)
    
    ##solvingTest
    def testForce(self,setNumber):
        self.ubongo(setNumber)
        self.test = deepcopy(self.solved)

    def clearTest(self):
        self.test = deepcopy(self.matrix)
        self.restorePieces()
    
    def fillTest(self):
        for i in self.test:
            for j in i:
                if j == 0:
                    return False
        return True

    def testPiece(self,pu_row,pu_col,piece):
        pu_rows = len(self.test)
        pu_cols = len(self.test[0])
        pi_rows = piece.height
        pi_cols = piece.width
        pu_col -= piece.start_col()
        if pu_col >= 0 and pu_row+pi_rows-1 < pu_rows and pu_col+pi_cols-1 < pu_cols:
            for i in range(pi_rows):
                for j in range(pi_cols):
                    if piece.matrix[i][j] == 1 and self.test[pu_row+i][pu_col+j] > 0:
                        return False
            return True
        else:
            return False
    
    def fillTestPiece(self,pu_row,pu_col,piece,index):
        pi_rows = piece.height
        pi_cols = piece.width
        pu_col -= piece.start_col()
        for i in range(pi_rows):
                for j in range(pi_cols):
                    if piece.matrix[i][j] == 1:
                        self.test[pu_row+i][pu_col+j] = index+2




puzzle0 = Puzzle([[0,0,0,0,1],[1,0,0,0,1],[1,0,0,0,0],[1,1,0,0,1]])
puzzle0.sets = [
    [piece7,piece4,piece11],
    [piece8,piece4,piece9],
    [piece9,piece6,piece10],
    [piece0,piece1,piece4],
    [piece2,piece8,piece4],
    [piece8,piece3,piece7]]

puzzle1 = Puzzle([[0,0,1,1],[0,0,0,0],[0,0,0,1],[0,0,0,0]])
puzzle1.sets = [
    [piece6,piece11,piece4],
    [piece9,piece1,piece10],
    [piece2,piece9,piece4],
    [piece8,piece4,piece2],
    [piece6,piece10,piece9],
    [piece9,piece6,piece8]]

puzzle2 = Puzzle([[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
puzzle2.sets = [
    [piece5,piece1,piece9,piece2],
    [piece9,piece4,piece3,piece5],
    [piece10,piece11,piece3,piece9],
    [piece6,piece10,piece9,piece5],
    [piece11,piece0,piece10,piece4],
    [piece8,piece3,piece11,piece9]]

puzzle3 = Puzzle([[1,0,0,0,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]])
puzzle3.sets = [
    [piece7,piece11,piece8,piece4],
    [piece11,piece3,piece4,piece1],
    [piece1,piece6,piece4,piece5],
    [piece0,piece7,piece8,piece1],
    [piece6,piece0,piece4,piece10],
    [piece10,piece9,piece8,piece4]]

puzzle4 = Puzzle([[1,0,0,1,1],[0,0,0,1,1],[0,0,0,0,1],[1,0,0,0,0]])
puzzle4.sets = [
    [piece10,piece8,piece4],
    [piece8,piece9,piece1],
    [piece6,piece4,piece0],
    [piece9,piece8,piece6],
    [piece8,piece2,piece1],
    [piece3,piece1,piece9]]

puzzle5 = Puzzle([[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
puzzle5.sets = [
    [piece9,piece0,piece7,piece4],
    [piece2,piece8,piece9,piece1],
    [piece10,piece1,piece8,piece3],
    [piece0,piece4,piece3,piece6],
    [piece1,piece0,piece6,piece10],
    [piece3,piece2,piece4,piece9]]


puzzle6 = Puzzle([[1,0,0,1],[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,1,1]])
puzzle6.sets = [
    [piece0,piece11,piece1,piece6],
    [piece2,piece8,piece0,piece4],
    [piece5,piece10,piece4,piece7],
    [piece1,piece3,piece9,piece0],
    [piece4,piece11,piece8,piece9],
    [piece9,piece5,piece6,piece4]]


puzzle7 = Puzzle([[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,1,1]])
puzzle7.sets = [
    [piece6,piece9,piece1,piece11],
    [piece3,piece10,piece8,piece4],
    [piece10,piece9,piece7,piece2],
    [piece3,piece10,piece4,piece9],
    [piece9,piece0,piece7,piece6],
    [piece2,piece10,piece4,piece9]]

puzzle8 = Puzzle([[0,0,0,0,1],[1,0,0,0,1],[1,0,0,0,0],[1,1,0,0,1]])
puzzle8.sets = [
    [piece7,piece4,piece11],
    [piece8,piece4,piece9],
    [piece9,piece6,piece10],
    [piece0,piece1,piece4],
    [piece2,piece8,piece4],
    [piece8,piece3,piece7]]

puzzle9 = Puzzle([[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,1,1,1,1]])
puzzle9.sets = [
    [piece2,piece4,piece10],
    [piece9,piece10,piece4],
    [piece1,piece8,piece2],
    [piece11,piece4,piece1],
    [piece9,piece2,piece4],
    [piece8,piece9,piece4]]


puzzle10 = Puzzle([[0,0,0,1,1],[1,0,0,1,1],[1,0,0,0,0],[1,0,0,0,0]])
puzzle10.sets = [
    [piece9,piece4,piece10],
    [piece8,piece10,piece4],
    [piece10,piece7,piece9],
    [piece9,piece6,piece2],
    [piece0,piece1,piece6],
    [piece6,piece3,piece9]]
