import pygame
from network import Network
import pickle


pygame.init()
width = 700
height = 700
white = (255,255,255)
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")
clock = pygame.time.Clock()

tileExample = pygame.image.load('sprites/bamboo/01.png')

def tile(x,y):
    defaultX = 150
    defaultY = 200
    pygame.draw.rect(win, white, pygame.Rect(x,y,int(defaultX/3), int(defaultY/3)))
    TileSizeC = pygame.transform.scale(tileExample, (int(defaultX/3), int(defaultY/3)))
    win.blit(TileSizeC,(x,y))

def fillingSlots():
    slots = []
    for i in range(15):
        #hmmm do i still need slots array?
        slots.append(int(width/14) * i)
        tile(int(width/14) * i, height *0.8)
    #make it the same to the game cards / player's hand

def redrawWindow():
    win.fill((20,225,20))
    pygame.display.update()

def main():

    finished = False
    while not finished:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


        
        # tile(width*0.45, height *0.8)       
        redrawWindow()
        fillingSlots()
        clock.tick(60)

    pygame.quit()

main()