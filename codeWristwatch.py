"""Simulation of the Game: the wristwatch. The player deals a normal deck of 52 cards. Deals cards to 12 hours of a clock and extra card in the middle. Keeps dealing till out of cards or wins. If the card value matches hour value(Ace= 1...King=13) first return the cards dealt to this hour to bottom of deck and then place the card on the hour. This hour is now complete and will be skipped in subsequent deals. If all hours are complete player wins. In this program 0=Ace 1=2 and so on up to 12=King. Since suits do not affect the game, the deck then continues with 14-52, and are counted modulo 13. Tests for the classes except for Game are found at end. Validity of Game can be seen by uncommenting the 3 printlines in Game Class as per instruction there..."""

# import modules
import random

class Deck:
    """Our playdeck...note that 0=A, 1=2...,13=K and that cards are counted modulo 13 later in the game"""
    def addCards(self,listOfCards):
        #adds a list of cards to the deck and shuffles
        self.deck.extend(listOfCards)
    def deal(self):
        #deals a card from top of deck
        return self.deck.pop(0)
    def __init__(self):
        #create a deck of 52 cards to get the actual card just count modulo 13. 		
	#Ace is 0, the card 2 is 1 and so on
        #up to king which is 12.
        self.deck = list(range(0,52))
        # shuffle the cards
        random.shuffle(self.deck)
class Watch:
    """make a wristwatch structure consisting of 13 empty numbered hour objects
    the nonsolved vector lets us deactivate hours after they have been solved"""
    def __init__(self):
        self.h=[0,1,2,3,4,5,6,7,8,9,10,11,12]
        for i in range(0,13):
            self.h[i]=Hours(i)
            self.nonSolvedHours=[0,1,2,3,4,5,6,7,8,9,10,11,12]

class Hours:
    """makes an hour structure for our watch where we can place cards and remove all of them"""
    def __init__(self,i):
        self.cards=list()
        self.time=i
    def addCard(self,card):
        self.cards.append(card)
    def removeCards(self):
        self.cards=list()

class Game:
    def round(self):
        time=0
        #the game has 2 endstates: either we run out of cards or the hours all get solved
        while(len(self.deckOfCards.deck)>0 and len(self.wristWatch.nonSolvedHours)>0):
            #Uncomment the print functions below to follow a full round of the game
            #print("the deck:",self.deckOfCards.deck, "unsolved hours:",self.wristWatch.nonSolvedHours)
            #for i in range(0, 13):
            #   print("hour",self.wristWatch.h[i].time,self.wristWatch.h[i].cards)
            topCard=self.deckOfCards.deal()
            index=self.wristWatch.nonSolvedHours.index(time)
            if(topCard % 13==time):
                #this if loop is triggered if the value of the card matches the hour
                #in this case the cards already in that hour are put at the back of the deck and
                #the current matching card is placed in the hour instead.
                self.deckOfCards.addCards(self.wristWatch.h[time].cards)
                self.wristWatch.h[time].removeCards()
                self.wristWatch.h[time].addCard(topCard)
                self.wristWatch.nonSolvedHours.remove(time)
                #since we hit with 1 hour, it is possible that there are no more unsolved hours
                #if there are more, we move to the next hour on our watch
                if( len(self.wristWatch.nonSolvedHours))>0:
                    time=self.wristWatch.nonSolvedHours[(index)%len(self.wristWatch.nonSolvedHours)]
            else:
                #If we the card didn't match the hour, we simply place the card in the hour and move on to the next hour
                self.wristWatch.h[time].addCard(topCard)
                time=self.wristWatch.nonSolvedHours[(index+1)%len(self.wristWatch.nonSolvedHours)]
    def __init__(self):
        self.deckOfCards=Deck()
        self.wristWatch=Watch()


def gameTester():
    j=0/Users/martinskoglund1/Desktop/codeWristwatch.py
    n=100000
    #we let the game play n times and simply see what percentage of times the wristwatch solves completely
    for i in range(0,n):
        G=Game()
        G.round()
        if(len(G.wristWatch.nonSolvedHours)==0):
            j=j+1
    p=(j/1.0)/n
    print ("runs:", n)
    print ("total wins:", j)
    print ("Probability of winning:", p)

gameTester()


#some test functions to see if things work as they should. To let them run uncomment the two last lines of code.

def testDeck():
    d1=Deck()
    print("TESTTING DEAL...The Deck ", d1.deck)
    i=0
    while len(d1.deck)>0:
        print("Top Card is:", d1.deal())
        print ("Deck without top card:", d1.deck)
        i=i+1
    print ("Total cards popped", i)
    d1=Deck()
    print('TESTING addCARDS to bottom of deck. NEW DECK:', d1.deck)
    lList=list()
    for i in range(0,10):
        lList.append(d1.deal())
    print("List of 10 cards from top of deck", lList)
    print("The deck with 10 top cards removed", d1.deck)
    d1.addCards(lList)
    print("The deck w the 10 cards added to bottom", d1.deck)

def testWatchAndHours():
    w=Watch()
    print("Unsolved hours at start:", w.nonSolvedHours)
    for hours in w.h:
        print("hours at start(blank lists of cards):", hours.cards)
    d1=Deck()
    print (d1.deck)
    for i in range(0,13):
        w.h[i].addCard(d1.deal())
        w.h[i].addCard(d1.deal())
    for hours in w.h:
        print("hours after adding 2 cards to each:", hours.cards)
        print("My time is:", hours.time)
    for i in range(0,13):
        w.h[i].removeCards()
    for hours in w.h:
        print("hours after removing the cards:", hours.cards)
        print("My time is:", hours.time)


#testDeck()
#testWatchAndHours()
