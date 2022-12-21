
import random

import pygame
from pygame.locals import *

class tile(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.suit))

        
class tileWall(object):
    def __init__(self):
        self.tiles = []
        self.discardPile = []
        self.build()
    
    def build(self):
        #building number tiles
        for type in ["bamboo","dots","chinese"]:
            for number in range(1,10):
                # each number have 4 repetition
                for repeats in range(1,5):
                    self.tiles.append(tile(type,number))

        #building wind tiles, i just used 0 for value in honor tiles
        for type in ["north","south","east","west","red dragon","white dragon","green dragon"]:
            for v in range(1,5):
                self.tiles.append(tile(type,0))

        # building flowers
        for flower in ["chinese flower","english flower"]:
            for num in range(1,5):
                self.tiles.append(tile(flower,num))

    def wash(self):
        for i in range(len(self.tiles)-1,0,-1):
            rand = random.randint(0, i)
            #wash by swapping two tiles to make a random tilewall
            self.tiles[i], self.tiles[rand] = self.tiles[rand], self.tiles[i] 

    def show(self):
        for t in self.tiles:
            t.show()
        # print("length is :", len(self.tiles))
    
    def drawTile(self):
        return self.tiles.pop()

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self, tileWall):
        self.hand.append(tileWall.drawTile())
        return self

    def showHand(self):
        for tile in self.hand:
            tile.show()

    def discard(self, tileWall):
        tileWall.discardPile.append(self.hand[-1])
        return self.hand.pop()


# FirstTile = tile("bamboo",3)
# FirstTile.show()
Tiles = tileWall()
Tiles.wash()
Tiles.show()
# P1 = Player("player1")
# P1.draw(Tiles)
# P1.draw(Tiles)
# P1.showHand()


size = width, height = (500,500)

pygame.init()
running = True
# set window size
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Mahjong")
# set background colour
screen.fill((60,220,0))
pygame.draw.rect(screen,
(50, 50 ,50),
(width/2,0, (20), 20))
# draw graphics
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
