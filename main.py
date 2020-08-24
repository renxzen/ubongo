import os
import random

import pygame, sys

from button import *
from gameboard import *

mainFolder = os.path.dirname(__file__)
imgFolder = os.path.join(mainFolder,"images")

pygame.init()

screen = pygame.display.set_mode((750,500))

#fonts
fontDefault = pygame.font.SysFont(None,20)
fontTitle = pygame.font.SysFont(None,30)
fontTimer = pygame.font.SysFont(None,60)
fontTimer2 = pygame.font.SysFont(None,40)
fontGems = pygame.font.SysFont(None,20)


icon = pygame.image.load(os.path.join(imgFolder,"icon.jpg"))
background = pygame.image.load(os.path.join(imgFolder,"background.jpg"))
insbackground = pygame.image.load(os.path.join(imgFolder,"instructions.jpg"))
gamebackground = pygame.image.load(os.path.join(imgFolder,"gamebackground.jpg"))
solvingbackground = pygame.image.load(os.path.join(imgFolder,"canvas.jpg"))
winnerbackground = pygame.image.load(os.path.join(imgFolder,"victory.png"))
loserbackground = pygame.image.load(os.path.join(imgFolder,"gameover.png"))

gemBlue = pygame.image.load(os.path.join(imgFolder,"gemBlue.png"))
gemBlue = pygame.transform.scale(gemBlue, (22, 22))
gemGreen = pygame.image.load(os.path.join(imgFolder,"gemGreen.png"))
gemGreen = pygame.transform.scale(gemGreen, (22, 22))
gemOrange = pygame.image.load(os.path.join(imgFolder,"gemOrange.png"))
gemOrange = pygame.transform.scale(gemOrange, (22, 22))
gemPurple = pygame.image.load(os.path.join(imgFolder,"gemPurple.png"))
gemPurple = pygame.transform.scale(gemPurple, (22, 22))
gemRed = pygame.image.load(os.path.join(imgFolder,"gemRed.png"))
gemRed = pygame.transform.scale(gemRed, (22, 22))
gemYellow = pygame.image.load(os.path.join(imgFolder,"gemYellow.png"))
gemYellow = pygame.transform.scale(gemYellow, (22, 22))
playerOne = pygame.image.load(os.path.join(imgFolder,"player1.png"))
playerOne = pygame.transform.scale(playerOne, (22, 22))
playerTwo = pygame.image.load(os.path.join(imgFolder,"player2.png"))
playerTwo = pygame.transform.scale(playerTwo, (22, 22))

dice0 = pygame.image.load(os.path.join(imgFolder,"dice0.png"))
dice1 = pygame.image.load(os.path.join(imgFolder,"dice1.png"))
dice2 = pygame.image.load(os.path.join(imgFolder,"dice2.png"))
dice3 = pygame.image.load(os.path.join(imgFolder,"dice3.png"))
dice4 = pygame.image.load(os.path.join(imgFolder,"dice4.png"))
dice5 = pygame.image.load(os.path.join(imgFolder,"dice5.png"))

pygame.display.set_caption("Ubongo - Mondragon - Gallegos - Kuylen")
pygame.display.set_icon(icon)

###Botones
#menu
butStart = Button(281,340,187,60,(0,0,0),(190,190,190),"Empezar Juego",25,(255,255,255),(0,0,0))
butInst = Button(281,420,187,60,(0,0,0),(190,190,190),"Instrucciones",25,(255,255,255),(0,0,0))
#instrucciones
butInstBack = Button(125,420,187,60,(0,0,0),(190,190,190),"Volver",25,(255,255,255),(0,0,0,0))
#tablero
butDice = Button(300,432,130,60,(0,0,0),(190,190,190),"Tirar Dado",25,(255,255,255),(0,0,0))
butSolve = Button(300,432,130,60,(0,0,0),(190,190,190),"Resolver",25,(255,255,255),(0,0,0))
butGameOver = Button(525,460,90,30,(0,0,0),(190,190,190),"GameOver",25,(255,255,255),(0,0,0))
butSlot0 = Button(20,55,86,17,(0,0,0),(20,55,86,17))
butSlot1 = Button(20,75,86,17,(0,0,0),(20,75,86,17))
butSlot2 = Button(20,98,86,17,(0,0,0),(20,95,86,17))
butSlot3 = Button(20,119,86,17,(0,0,0),(20,115,86,17))
butSlot4 = Button(20,140,86,17,(0,0,0),(20,136,86,17))
butSlot5 = Button(20,161,86,17,(0,0,0),(20,157,86,17))
#resolver
butUbongo = Button(560,420,140,35,(0,0,0),(190,190,190),"UBONGO!",25,(255,255,255),(0,0,0,0))
butPasar = Button(560,380,140,35,(0,0,0),(190,190,190),"Pasar!",25,(255,255,255),(0,0,0,0))
butClear = Button(480,420,50,35,(0,0,0),(190,190,190),"X",25,(255,255,255),(0,0,0,0))
butTest = Button(480,40,50,35,(0,0,0),(190,190,190),"Test",25,(255,255,255),(0,0,0,0))
#GameOver
butGoBack = Button(281,420,187,50,(0,0,0),(190,190,190),"Menu Principal",25,(255,255,255),(0,0,0,0))

#timer
clock = pygame.time.Clock()
current_time = 0

goToStart = False


def drawText(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

def main_menu():
    global goToStart
    while True:
        if goToStart:
            goToStart = False

        mx, my = pygame.mouse.get_pos()
        #pygame.time.delay(1000)

        screen.fill((255,255,255))
        screen.blit(background,(0,0))

        #stringy = str(mx) + "  " + str(my)
        #drawText(stringy,fontDefault,(0,0,0),screen,0,0)

        butStart.draw(screen,(mx,my))
        butInst.draw(screen,(mx,my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                
            if event.type == pygame.MOUSEBUTTONUP:
                if butStart.isOver((mx,my)):
                    game()
                if butInst.isOver((mx,my)):
                    instructions()
        
        pygame.display.update()

def instructions():
    run = True
    while run:
        mx, my = pygame.mouse.get_pos()

        screen.fill((255,255,255))
        screen.blit(insbackground,(0,0))

        butInstBack.draw(screen,(mx,my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if butInstBack.isOver((mx,my)):
                    run = False
        
        pygame.display.update()

def game():
    global goToStart
    global current_time
    clock.tick(60)
    
    newGame = gameBoard()

    run = True
    while run:
        #go back to menu
        if goToStart:
            run = False

        mx, my = pygame.mouse.get_pos()

        butSlot0.draw(screen,(mx,my))
        butSlot1.draw(screen,(mx,my))
        butSlot2.draw(screen,(mx,my))
        butSlot3.draw(screen,(mx,my))
        butSlot4.draw(screen,(mx,my))
        butSlot5.draw(screen,(mx,my))
        
        screen.fill((255,255,255))
        screen.blit(gamebackground,(0,0))

        #stringy = str(mx) + "  " + str(my)
        #drawText(stringy,fontDefault,(0,0,0),screen,0,0)

        #buttons
        butDice.draw(screen,(mx,my),(255,255,255))
        butGameOver.draw(screen,(mx,my),(255,255,255))
        if newGame.startTimer: butSolve.draw(screen,(mx,my),(255,255,255))
        if newGame.startTimer:
            drawText(str(newGame.time + current_time - int(pygame.time.get_ticks()/1000)),fontTimer,(255,255,255),screen,685,445)
        else:
            drawText(str(newGame.time),fontTimer,(255,255,255),screen,685,445)
        

        #timer computer wins
        #if newGame.time + current_time - int(pygame.time.get_ticks()/1000) < 15 and newGame.startTimer and not newGame.ubongo:
        #    newGame.players[1].movesleft = 2
        #    newGame.aiMove()
        #    newGame.players[1].movesleft = 0
        if newGame.aiWinner == True:
            #pygame.time.wait(1000)
            newGame.aiWinner = False
            newGame.aiMove()
            newGame.endRound()


        #timer round ends
        if (newGame.time + current_time - int(pygame.time.get_ticks()/1000)) == 0 and newGame.startTimer:
            newGame.aiMove()
            newGame.endRound()
        
        #draw players
        starty = 50
        for i in range(6):
            startx = 35
            for j in range(0,2):
                if newGame.theBoard.matrix[i][j] == 10: screen.blit(playerOne,(startx,starty))
                if newGame.theBoard.matrix[i][j] == 11: screen.blit(playerTwo,(startx,starty))
                startx += 42
            starty += 22

        #draw board gems
        starty = 45
        for i in range(6):
            startx = 122
            for j in range(2,14):
                if newGame.theBoard.matrix[i][j] == 0: screen.blit(gemRed,(startx,starty))
                if newGame.theBoard.matrix[i][j] == 1: screen.blit(gemBlue,(startx,starty))
                if newGame.theBoard.matrix[i][j] == 2: screen.blit(gemYellow,(startx,starty))
                if newGame.theBoard.matrix[i][j] == 3: screen.blit(gemOrange,(startx,starty))
                if newGame.theBoard.matrix[i][j] == 4: screen.blit(gemPurple,(startx,starty))
                if newGame.theBoard.matrix[i][j] == 5: screen.blit(gemGreen,(startx,starty))
                startx += 42
            starty += 22

        #imprimir Turnos
        stringTurnos = "Turnos: "+str(newGame.turns)
        drawText(stringTurnos,fontGems,(255,255,255),screen,535,435)

        #gems player1
        drawText(str(newGame.players[0].gems[0]),fontGems,(255,255,255),screen,30,455)
        drawText(str(newGame.players[0].gems[3]),fontGems,(255,255,255),screen,30,478)
        drawText(str(newGame.players[0].gems[1]),fontGems,(255,255,255),screen,75,455)
        drawText(str(newGame.players[0].gems[4]),fontGems,(255,255,255),screen,75,478)
        drawText(str(newGame.players[0].gems[2]),fontGems,(255,255,255),screen,115,455)
        drawText(str(newGame.players[0].gems[5]),fontGems,(255,255,255),screen,115,478)
        drawText(str(newGame.players[0].movesleft),fontGems,(255,255,255),screen,115,432)

        

        #gems player2
        drawText(str(newGame.players[1].gems[0]),fontGems,(255,255,255),screen,185,455)
        drawText(str(newGame.players[1].gems[3]),fontGems,(255,255,255),screen,185,478)
        drawText(str(newGame.players[1].gems[1]),fontGems,(255,255,255),screen,230,455)
        drawText(str(newGame.players[1].gems[4]),fontGems,(255,255,255),screen,230,478)
        drawText(str(newGame.players[1].gems[2]),fontGems,(255,255,255),screen,270,455)
        drawText(str(newGame.players[1].gems[5]),fontGems,(255,255,255),screen,270,478)
        drawText(str(newGame.players[1].movesleft),fontGems,(255,255,255),screen,270,432)
 
        #dice faces
        if newGame.theDice.face == 0: screen.blit(dice0,(445,432))
        if newGame.theDice.face == 1: screen.blit(dice1,(445,432))
        if newGame.theDice.face == 2: screen.blit(dice2,(445,432))
        if newGame.theDice.face == 3: screen.blit(dice3,(445,432))
        if newGame.theDice.face == 4: screen.blit(dice4,(445,432))
        if newGame.theDice.face == 5: screen.blit(dice5,(445,432))

        #draw Puzzles And Pieces
        if newGame.startTimer and not newGame.ubongo and not newGame.aiWinner:
            drawText("Puzzle",fontTitle,(0,0,0),screen,65,210)
            starty = 230
            for i in range(newGame.puzzles[newGame.selectedPuzzle].height):
                startx = 30
                for j in range(newGame.puzzles[newGame.selectedPuzzle].width):
                    if newGame.puzzles[newGame.selectedPuzzle].matrix[i][j] == 0:
                        pygame.draw.rect(screen,(0,0,0),(startx,starty,30,30),0)
                        pygame.draw.rect(screen,(255,255,255),(startx+1,starty+1,28,28),0)
                    startx += 30
                starty += 30

            initx= 230
            for index in range(len(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet])):
                auxstring = "Pieza " + str(index+1)
                drawText(auxstring,fontTitle,(0,0,0),screen,initx,210)
                starty = 230
                for i in range(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].height):
                    startx = initx
                    for j in range(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].width):
                        if newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].matrix[i][j] == 1:
                            pygame.draw.rect(screen,(0,0,0),(startx,starty,30,30),0)
                            pygame.draw.rect(screen,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].color,(startx+1,starty+1,28,28),0)
                        startx += 30
                    starty += 30
                initx += 120
        
        #Ubongo - print solutions
        if newGame.ubongo or newGame.aiWinner:
            newGame.puzzles[newGame.selectedPuzzle].ubongo(newGame.selectedSet)

            drawText("Computadora",fontTitle,(0,0,0),screen,65,210)
            starty = 230
            for i in range(newGame.puzzles[newGame.selectedPuzzle].height):
                startx = 30
                for j in range(newGame.puzzles[newGame.selectedPuzzle].width):
                    for k in range(len(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet])):
                        if newGame.puzzles[newGame.selectedPuzzle].solved[i][j] == k+2:
                            pygame.draw.rect(screen,(0,0,0),(startx,starty,30,30),0)
                            pygame.draw.rect(screen,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][k].color,(startx+1,starty+1,28,28),0)
                    startx += 30
                starty += 30
            if newGame.ubongo:
                drawText("Jugador",fontTitle,(0,0,0),screen,365,210)
                starty = 230
                for i in range(newGame.puzzles[newGame.selectedPuzzle].height):
                    startx = 330
                    for j in range(newGame.puzzles[newGame.selectedPuzzle].width):
                        for k in range(len(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet])):
                            if newGame.puzzles[newGame.selectedPuzzle].test[i][j] == 0:
                                pygame.draw.rect(screen,(0,0,0),(startx,starty,30,30),0)
                                pygame.draw.rect(screen,(255,255,255),(startx+1,starty+1,28,28),0)
                            if newGame.puzzles[newGame.selectedPuzzle].test[i][j] == k+2:
                                pygame.draw.rect(screen,(0,0,0),(startx,starty,30,30),0)
                                pygame.draw.rect(screen,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][k].color,(startx+1,starty+1,28,28),0)
                        startx += 30
                    starty += 30



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                if butSolve.isOver((mx,my)) and newGame.startTimer:
                    solvingpuzzle(newGame,newGame.time + current_time)
                if butDice.isOver((mx,my)) and not newGame.startTimer:
                    current_time = int(pygame.time.get_ticks()/1000)
                    newGame.throwDice()
                if butGameOver.isOver((mx,my)):
                    newGame.getWinner()
                    gameOver(newGame)
        
                if butSlot0.isOver((mx,my)) and newGame.ubongo:
                    newGame.movePlayer(0,0)
                    if newGame.players[0].moved:
                        newGame.aiMove()
                        newGame.endRound()
                if butSlot1.isOver((mx,my)) and newGame.ubongo:
                    newGame.movePlayer(0,1)
                    if newGame.players[0].moved:
                        newGame.aiMove()
                        newGame.endRound()
                if butSlot2.isOver((mx,my)) and newGame.ubongo:
                    newGame.movePlayer(0,2)
                    if newGame.players[0].moved:
                        newGame.aiMove()
                        newGame.endRound()
                if butSlot3.isOver((mx,my)) and newGame.ubongo:
                    newGame.movePlayer(0,3)
                    if newGame.players[0].moved:
                        newGame.aiMove()
                        newGame.endRound()
                if butSlot4.isOver((mx,my)) and newGame.ubongo:
                    newGame.movePlayer(0,4)
                    if newGame.players[0].moved:
                        newGame.aiMove()
                        newGame.endRound()
                if butSlot5.isOver((mx,my)) and newGame.ubongo:
                    newGame.movePlayer(0,5)
                    if newGame.players[0].moved:
                        newGame.aiMove()
                        newGame.endRound()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()

def solvingpuzzle(newGame, timing):
    run = True
    while run:
        mx, my = pygame.mouse.get_pos()

        screen.fill((255,255,255))
        screen.blit(solvingbackground,(0,0))

        #Timer
        drawText(str(timing - int(pygame.time.get_ticks()/1000)),fontTimer2,(0,0,0),screen,685,40)

        butUbongo.draw(screen,(mx,my))
        butPasar.draw(screen,(mx,my))
        butClear.draw(screen,(mx,my))
        butTest.draw(screen,(mx,my))

        #draw puzzle test
        starty = 100
        for i in range(newGame.puzzles[newGame.selectedPuzzle].height):
            startx = 490
            for j in range(newGame.puzzles[newGame.selectedPuzzle].width):
                for k in range(len(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet])):
                    if newGame.puzzles[newGame.selectedPuzzle].test[i][j] == 0:
                        pygame.draw.rect(screen,(0,0,0),(startx,starty,45,45),0)
                        pygame.draw.rect(screen,(255,255,255),(startx+1,starty+1,43,43),0)
                    if newGame.puzzles[newGame.selectedPuzzle].test[i][j] == k+2:
                        pygame.draw.rect(screen,(0,0,0),(startx,starty,45,45),0)
                        pygame.draw.rect(screen,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][k].color,(startx+1,starty+1,43,43),0)
                startx += 45
            starty += 45
        
        #draw pieces
        initx = 50
        inity = 50
        for index in range(len(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet])):
            starty = inity
            for i in range(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].height):
                startx = initx
                for j in range(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].width):
                    if newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].matrix[i][j] == 1:
                        pygame.draw.rect(screen,(0,0,0),(startx,starty,30,30),0)
                        pygame.draw.rect(screen,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][index].color,(startx+1,starty+1,28,28),0)
                    startx += 30
                starty += 30
            initx += 160
            if initx > 360:
                initx = 50
                inity = 200
        
        #draw selected piece
        if newGame.selectedPiece >= 0:
            starty = 385
            for i in range(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].height):
                startx = 170
                for j in range(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].width):
                    if newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].matrix[i][j] != 0:
                        pygame.draw.rect(screen,(0,0,0),(startx,starty,20,20),0)
                        pygame.draw.rect(screen,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].color,(startx+1,starty+1,18,18),0)
                    startx += 20
                starty += 20

        #color the puzzle with selection
        starty = 100
        for i in range(newGame.puzzles[newGame.selectedPuzzle].height):
            startx = 490
            for j in range(newGame.puzzles[newGame.selectedPuzzle].width):
                if mx > startx and mx < startx + 45:
                    if my > starty and my < starty + 45:
                        if newGame.puzzles[newGame.selectedPuzzle].test[i][j] != 1:
                            pygame.draw.rect(screen,(0,0,255),(startx+1,starty+1,43,43),0)
                startx += 45
            starty += 45

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                #UBONGO!
                if butUbongo.isOver((mx,my)):
                    if newGame.puzzles[newGame.selectedPuzzle].fillTest():
                        newGame.ubongoTrigger()
                        run = False

                #Pasar!
                if butPasar.isOver((mx,my)):
                    newGame.aiWon()
                    run = False
                
                #Limpiar Matriz
                if butClear.isOver((mx,my)):
                    newGame.puzzles[newGame.selectedPuzzle].clearTest()

                #Rellenar Puzzle
                if butTest.isOver((mx,my)):
                    newGame.puzzles[newGame.selectedPuzzle].testForce(newGame.selectedSet)
                
                #select piece and rotate
                initx = 50
                inity = 50
                for i in range(len(newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet])):
                    if mx > initx and mx < initx + newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][i].width*30:
                        if my > inity and my < inity + newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][i].height*30:
                            newGame.selectedPiece = i
                            newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].newRotate()
                    initx += 160
                    if initx > 360:
                        initx = 50
                        inity = 200
                
                ##place in puzzle
                if newGame.selectedPiece >= 0:
                    starty = 100
                    for i in range(newGame.puzzles[newGame.selectedPuzzle].height):
                        startx = 490
                        for j in range(newGame.puzzles[newGame.selectedPuzzle].width):
                            if mx > startx and mx < startx + 45:
                                if my > starty and my < starty + 45:
                                    #print Test
                                    #newGame.puzzles[newGame.selectedPuzzle].printTest()
                                    if newGame.puzzles[newGame.selectedPuzzle].testPiece(i,j,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece]):
                                        if not newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].selected:
                                            newGame.puzzles[newGame.selectedPuzzle].fillTestPiece(i,j,newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece],newGame.selectedPiece)
                                            newGame.puzzles[newGame.selectedPuzzle].sets[newGame.selectedSet][newGame.selectedPiece].selected = True
                                            newGame.selectedPiece = -1

                                    
                                    ##testPiece
                            startx += 45
                        starty += 45

                

            #if event.type == pygame.MOUSEMOTION:
        
        pygame.display.update()

def gameOver(newGame):
    global goToStart
    run = True
    while run:
        mx, my = pygame.mouse.get_pos()
        screen.fill((255,255,255))

        if newGame.winner:
            screen.blit(winnerbackground,(0,0))
        else:
            screen.blit(loserbackground,(0,0))

        butGoBack.draw(screen,(mx,my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if butGoBack.isOver((mx,my)):
                    goToStart = True
                    run = False
        
        pygame.display.update()


#INICIO JUEGO
main_menu()
