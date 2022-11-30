print("Hello World")
import random

class tile(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.suit))

        
class tileWall(object):
    def __init__(self):
        self.tiles = []
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

    def show(self):
        for t in self.tiles:
            t.show()
        print("length is :", len(self.tiles))

class Player(object):
    def __init__(self):
        pass

# FirstTile = tile("bamboo",3)
# FirstTile.show()
tileWall().show()
