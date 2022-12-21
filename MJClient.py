import pygame
from network import Network
import pickle


pygame.init()
width = 700
height = 700
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")
clock = pygame.time.Clock()

tileExample = pygame.image.load('sprites/bamboo/01.png')

def tile(x,y):
    defaultX = 150
    defaultY = 200
    TileSizeC = pygame.transform.scale(tileExample, (int(defaultX/2), int(defaultY/2)))
    win.blit(TileSizeC,(x,y))


finished = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


    win.fill((10,240,10))
    tile(width*0.45, height *0.8)            
    pygame.display.update()
    clock.tick(60)

pygame.quit()