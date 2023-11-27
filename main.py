# card game
from random import shuffle

# set up class for deck

class Deck(object):
    """
    Does not accept parameters
    
    This creates a 52 card deck to play the game
    """
    suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    rank_val = [None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    rank_names = [None, None, 'Two', 'Three', 'Four', 'Five',
                 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                 'Queen', 'King', 'Ace']
    index_tracker = {"i" : 0, "j" : 0} # tracking the i, j indices used later in round()
    def __init__(self):
        self.deck = []
        self.p1_deck = []
        self.p2_deck = []
        self.used_cards = []
        self.build()
        self.shuffle()
        self.deal()
    
    def build(self):
        """builds the deck of the game"""
        for i in self.suit:
            for j in self.rank_val[2:]:
                card = Card(j, i)
                self.deck.append(card)
                
    def shuffle(self):
        """shuffles the deck of the game"""
        shuffle(self.deck)
        print("Deck has been shuffled")

    def show(self):
        """displays the whole deck"""
        print(self.deck)
        
    def deal(self):
        """deals cards to both players"""
        self.p1_deck = self.deck[:26]
        self.p2_deck = self.deck[26:]
        print("Both players have been dealt 26 cards")

class Card(Deck):
    """
    Child class of Deck
    
    Has all the attributes regarding cards
    """
    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def __repr__(self):
        return self.rank_names[self.rank] + ' of ' + self.suit

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

class Game(Deck):
    """
    Child class of Deck
    
    Contains all methods used to power the game
    """
    def __init__(self):
        super().__init__() # init attributes of parent class
        
    def players(self):
        """
        Asks for player names
        """
        p1_name = str(input("Player 1 name -> "))
        p2_name = str(input("Player 2 name -> "))
        print(f"Welcome to war, {p1_name} and {p2_name}")

    def round(self):
        """
        Starts a new round for both players
        """
        while len(self.p1_deck) or len(self.p2_deck) > 0:
            roundcount = 1 # incremental
            try:
                startround = str(input(f"Start round {roundcount} ? (y/n)"))
            except(ValueError):
                print("Please only input either y or n")
                self.round()
            if startround == "y":
                proceed = True
            elif startround == "n":
                proceed = False
            else:
                print("Please only enter either y or n")
                self.round()
            
            # proceed = True --> round starts
            if proceed is False:
                print("Exiting game, losers")
                break

            if proceed is True:
                print(f"Player 1 card: {self.p1_deck[0]}\nPlayer 2 card: {self.p2_deck[0]}")
                
                # manipulate the index tracker dictionary
                i, j = self.index_tracker.values() # just taking the values and assigning to i, j
                print(f"i = {i}\nj = {j}")
                
                # 3 conditions to check, <, >, ==
                if self.p1_deck[i] > self.p2_deck[j]: # using i and j, modular
                    roundwin = "p1"
                    print(self.p1_deck[0] > self.p2_deck[0])
                    print("Player 1 wins this round")
                    self.p1_deck.append(self.p1_deck[0])
                    self.p1_deck.append(self.p2_deck[0])
                    self.p1_deck.pop(0) # make sure to remove top card from deck
                    self.p2_deck.pop(0)
                    print(f"p1 has {len(self.p1_deck)} cards") # debug
                    print(f"p2 has {len(self.p2_deck)} cards") # debug
                    
                elif self.p1_deck[i] < self.p2_deck[j]:
                    roundwin = "p2"
                    print(self.p1_deck[0] < self.p2_deck[0])
                    print("Player 2 wins this round")
                    self.p2_deck.append(self.p1_deck[0])
                    self.p2_deck.append(self.p2_deck[0])
                    self.p1_deck.pop(0) # make sure to remove top card from deck
                    self.p2_deck.pop(0)
                    print(f"p1 has {len(self.p1_deck)} cards") # debug
                    print(f"p2 has {len(self.p2_deck)} cards") # debug
                    
                elif (self.p1_deck[i] == self.p2_deck[j]) and (len(self.p1_deck) or len(self.p2_deck) > 3):
                    self.index_tracker["i"] = 2 # now i and j are mapped to 2, as we use the 3rd card for both decks here
                    self.index_tracker["j"] = 2 # this is only temporary, i and j are set back to 0 right after
                    self.round() # should now check for conditions using i and j as index
                    if roundwin == "p1":
                        self.p1_deck.append(self.p1_deck[1])
                        self.p1_deck.append(self.p1_deck[2])
                        self.p1_deck.pop(1)
                        self.p1_deck.pop(2)
                        self.p2_deck.pop(1)
                        self.p2_deck.pop(2)
                    elif roundwin == "p2":
                        self.p2_deck.append(self.p2_deck[1])
                        self.p2_deck.append(self.p2_deck[2])
                        self.p2_deck.pop(1)
                        self.p2_deck.pop(2)
                        self.p1_deck.pop(1)
                        self.p1_deck.pop(2)
                self.index_tracker["i"] = 0 # reset both i and j to 0 for further rounds
                self.index_tracker["j"] = 0 # should work just fine
                    

def wargame():
    """
    Starts a game of war
    """
    deck = Game()
    deck.round()