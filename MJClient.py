import pygame
from network import Network
import pickle


pygame.init()
width = 800
height = 700
white = (255,255,255)
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")
clock = pygame.time.Clock()

tileExample = pygame.image.load('sprites/bamboo/01.png')

class tile:
    def __init__(self,x,y):
        defaultX = 150
        defaultY = 200
        pygame.draw.rect(win, white, pygame.Rect(x,y,int(defaultX/3), int(defaultY/3)))
        TileSizeC = pygame.transform.scale(tileExample, (int(defaultX/3), int(defaultY/3)))
        win.blit(TileSizeC,(x,y))
        pygame.display.update()

def click(self, pos):
    x1 = pos[0]
    y1 = pos[1]
    ##check for whether the click is valid
    if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
        return True
    else:
        return False

def fillingSlots():
    slots = [] #contain the dimensions of the tiles
    for i in range(15):
        #hmmm do i still need slots array?
        slots.append(int(700/14) * i+25)
        tile(int(700/14) * i+25, height *0.8)
    #make it the same to the game cards / player's hand

def redrawWindow():
    win.fill((20,225,20))
    pygame.display.update()

def main():

    finished = False
    redrawWindow()
    while not finished:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


        
        # tile(width*0.45, height *0.8)       
        
        fillingSlots()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()