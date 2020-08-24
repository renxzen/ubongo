def deepcopy(a):
    b = [[a[i][j] for j in range(len(a[i]))] for i in range(len(a))]
    return b

class Piece:
    def __init__(self, matrix):
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.matrix = deepcopy(matrix)
        self.original = deepcopy(matrix)
        self.color = 0
        self.form = 0
        self.selected = False
        self.startRotating = False
    
    def redimension(self):
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def restore(self):
        self.matrix = deepcopy(self.original)
        self.redimension()

    def newRotate(self):
        if self.startRotating:
            if self.form == 3 or self.form > 6:
                self.flip()
                if self.form > 6:
                    self.form = 0
                else:
                    self.form += 1
            else:
                self.rotate()
                self.form += 1
        self.startRotating = True

    def rotate(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        rotated = [0] * cols
        for i in range(cols):
            aux = [0] * rows
            for j in range(rows):
                aux[j] = self.matrix[rows - 1 - j][i]
            rotated[i] = aux
        self.matrix = deepcopy(rotated)
        self.redimension()
    
    def flip(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        flipped = [0] * rows
        for i in range(rows):
            aux = [0] * cols
            for j in range(cols):
                aux[j] = self.matrix[i][cols - 1 - j]
            flipped[i] = aux
        self.matrix = deepcopy(flipped)
        self.redimension()
    
    def start_col(self):
        n = len(self.matrix[0])
        for i in range(n):
            if self.matrix[0][i] == 1:
                return i
    
    def print(self):
        for i in self.matrix:
            print(i)


piece0 = Piece([[1,1],[1,0]])
piece1 = Piece([[1,0],[1,0],[1,1],[1,0]])
piece2 = Piece([[1],[1],[1],[1]])
piece3 = Piece([[1,1],[1,1]])
piece4 = Piece([[0,1],[1,1],[1,1]])
piece5 = Piece([[1],[1]])
piece6 = Piece([[1,1],[1,0],[1,0],[1,0]])
piece7 = Piece([[1,1,0],[0,1,0],[0,1,1]])
piece8 = Piece([[0,1],[1,1],[1,0]])
piece9 = Piece([[1,1],[0,1],[0,1]])
piece10 = Piece([[1,0],[1,1],[1,0]])
piece11 = Piece([[1],[1],[1]])

piece0.color = (225,27,129)
piece1.color = (105,31,150)
piece2.color = (11,221,242)
piece3.color = (29,126,45)
piece4.color = (57,49,60)
piece5.color = (218,143,63)
piece6.color = (25,83,226)
piece7.color = (88,63,33)
piece8.color = (126,232,113)
piece9.color = (207,220,53)
piece10.color = (206,52,244)
piece11.color = (231,38,61)

'''
0 = rosa
1 = morado
2 = celeste
3 = verde
4 = gris
5 = naranja
6 = azul
7 = marron
8 = verde limon
9 = amarillo
10 = lila
11 = rojo



'''