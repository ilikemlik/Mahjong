import random

## this is where to put the logic of the game

# def player(self, turn, player):
#     ## making of the turns
#     if player == turn:
#         if player == 1:
#             self.p1turn = True
#             self.p4turn = False
#         if player == 2:
#             self.p2turn = True
#             self.p1turn = False
#         if player == 3:
#             self.p3turn = True
#             self.p2turn = False
#         if player == 4:
#             self.p4turn = True
#             self.p3turn = False

class tile(object):
    def __init__(self, suit, value, honor):
        self.suit = suit
        self.value = value
        self.honor = honor

    def show(self):
        if self.honor == False:
            print("{} of {}".format(self.value,self.suit))
        elif self.honor == True:
            print("{}".format(self.suit))
        
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
                    self.tiles.append(tile(type,number,False))

        #building wind tiles, i just used 0 for value in honor tiles
        for type in ["north","south","east","west","red dragon","white dragon","green dragon"]:
            for v in range(1,5):
                self.tiles.append(tile(type,0,True))

        # building flowers
        for flower in ["wind flower","season flower"]:
            for num in range(1,5):
                self.tiles.append(tile(flower,num,False))

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

    def diceRoll(self):
        y1 = random.randint(1,6)
        y2 = random.randint(1,6)
        Dices = y1+y2
        print("second roll: ", y2,"| first roll: ", y1)
        print("total roll: ", Dices)
        return Dices

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
    
    def startingHand(self, tileWall):
        for i in range(0,4):
            self.draw(tileWall)


# FirstTile = tile("bamboo",3)
# FirstTile.show()

# P1 = Player("player1")
# P1.draw(Tiles)
# P1.draw(Tiles)
# P1.showHand()

def main():
    Tiles = tileWall()
    Tiles.wash()
    Tiles.show()
    Tiles.diceRoll()
    p1 = Player("player1")
    p2 = Player("player2")
    p3 = Player("player3")
    p4 = Player("player4")

    ## starting hand draw
    for i in range(0,3):
        p1.startingHand(Tiles)
        p2.startingHand(Tiles)
        p3.startingHand(Tiles)
        p4.startingHand(Tiles)
        
    p1.draw(Tiles)
    p2.draw(Tiles)
    p3.draw(Tiles)
    p4.draw(Tiles)


    # p1.showHand()
    # print()
    # Tiles.show()

    ## start of Game~~

    # flowers get exchange for tiles
    
    # player 1 is current player
    # player 1 checks for winning hand
    
    ## repeat from here
    # current player draws tile
    p1.draw(Tiles)
    # check for presence of win
    # current player throws tile

    # time for whether pong or if next player wants to chow

    # current player = player 2/++, player 2 draws 

    ## if other player pongs ( previous players get skip )
    # that player becomes current player

    ## repeat until win

main()

