import pygame

class Button():
    def __init__(self, x, y, width, height, color, hlcolor,  text='', tsize = 20, tcolor = None, thlcolor = None):
        self.color = color
        self.ogcolor = color
        self.hlcolor = hlcolor

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.tsize = tsize

        self.tcolor = tcolor
        self.togcolor = tcolor
        self.thlcolor = thlcolor

    def draw(self,win,pos=None,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont(None, self.tsize)
            text = font.render(self.text, 1, self.tcolor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
        if pos:
            if self.isOver(pos):
                self.color = self.hlcolor
                self.tcolor = self.thlcolor
            else:
                self.color = self.ogcolor
                self.tcolor = self.togcolor

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False