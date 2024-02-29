#!/usr/bin/env python3

import random

rules = """ 
    This is a deck and a half Pinochle card game.
    There are 4 players in teams of two.
    There is a kitty that comes with a winning bid which consists of 4 cards. 
    There is a rotating dealer button going clockwise.
    The initial bid is done by the player to the left of the dealer.
    Initial bid starts at '41'
    Each player can bid higher than the previous or pass.
    There is no limit on bid increment amount per bid.
    The process keeps going to the next person until all others have passed.
    If no player bids on the initial amount, a second bidding process starts 
     at 40. Players may take it or not, but cannot bid higher. 
        NOTE: There are two ways to deal with no one bidding:
        1) Fold all hands and move the starting position to the next player
        2) Require the dealer
    Kitty cards are shown to every player upon a winning bid.
    The winner of the bid takes the 4 cards and discards 4 cards.
    The winner then names a trump suit.
    ANY TRUMP OR ACES will be shown to all players if discarded.
    Each player chooses their meld and lays it on the table.
    Points come from a mixture of meld and counters.
    Whoever takes the trick, takes all cards therein; however, not all card
     are worth points.  Only K, T(10), A are worth a point.
    NOTE that the order of cards is 9, J, Q, K, T(10), A.
    The last trick taken is worth a point for the trick itself.
    At the end of each round, the team which wins the bid, must have equal or 
     more points than were bid.  If they do not, they go set, and lose points 
     equal to the amount bid.
        ex1: winning bid is 45, team melds 25 and takes 22 points for 47 total.
             They have >= 45, so they get 47 points. 
        ex2: winning bid is 45, team melds 22 and takes 22 points for 44 total.
             They do not have >= 45 and have gone set, so they lose 45 points. 
    First team to 250 points wins the game.
    In the event that both teams go over 250 points in the same round, the team 
     that won the bid wins the game.
    """

def get_player_count():
    keep_going = [str(range(4))]
    num_players = input('How many players? Press \'q\' to (q)uit' )
    #match

class Card:
    def __init__(self, suit, denomination, strength, pointValue) -> None:
        self.suit = suit
        self.denomination = denomination
        self.strength = strength
        self.pointValue = pointValue

    def __str__(self) -> str:
        # NOTE ANSI escape char (\033) does NOT count towards string length
        terminal_colors = "\033[30m\033[47m" if self.suit in ["♣", "♠"] else \
                ("\033[31m\033[47m" if self.suit in ["♦", "♥"] else "\033[30m")
        return f"{terminal_colors}{self.denomination}{self.suit}\033[0m"
        # str(Card)[10:12] gives the denomination and suit as one string
        # `d, s = str(Card)[10:12]` gives the denomination and suit seperately

    def __repr__(self) -> str:
        # NOTE ANSI escape char (\033) does NOT count towards string length
        terminal_colors = "\033[30m\033[47m" if self.suit in ["♣", "♠"] else \
                ("\033[31m\033[47m" if self.suit in ["♦", "♥"] else "\033[30m")
        return f"{terminal_colors}{self.denomination}{self.suit}\033[0m"
    
    def value(self):
        return int(self.pointValue)
     
    def strength(self):
        return int(self.strength)

    def suit(self):
        return self.suit

    def __lt__(self, other):
        #return str(self) > str(other)
        if game.trump_suit != None:
            _suits = Deck.suits[Deck.suits.index(game.trump_suit):] + \
                    Deck.suits[:Deck.suits.index(game.trump_suit)]
        else:
            _suits = Deck.suits.copy()
        return str(_suits.index(self.suit)) + str(self.strength) <  \
                str(_suits.index(other.suit)) + str(other.strength)
    def __eq__(self, other):
        return str(_suits.index(self.suit)) + str(self.strength) ==  \
                str(_suits.index(other.suit)) + str(other.strength)


    
# TODO: Make deck part of Game class and initialize on start.
# TODO: Make shuffle part of a new hand method.
class Game:
    def __init__(self, num_players=4) -> None:
        self.deck = Deck()
        self.players = [Player(f'Player {i+1}') for i in range(num_players)]
        # NOTE If number of players is below 4, add Bot to prevent bugs
        self.current_bid = 41
        self.kitty = []
        self.trump_suit = None
        self.lead_suit = None
        self.dealer = self.players[0]


    def play(self):
        pass

    def deal(self):
        self.deck.shuffle()
        while len(self.deck.cards) > 4:
            for player in players:
                player.hand.append(self.deck.cards.pop(0))
        self.kitty.extend(\
            [self.deck.cards.pop(0) for i in range(len(self.deck.cards))])

    def change_dealer(self):
        current_dealer_index = self.players.index(self.dealer)
        if self.players[current_dealer_index] != self.players[-1]:
            self.dealer = self.players[current_dealer_index+1]
        else:
            self.dealer = players[0]

class Deck:
    denominations = ["9", "J", "Q", "K", "T", "A"] # NOTE used T for 10
    suits = ["♦", "♣", "♥", "♠"] # Digraph is cC cD cH cS

    def __init__(self, num_decks=3) -> None:
        self.num_decks = num_decks
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        # TODO Add terminal colors - red and black - with background white
        strengths = {"9":0, "J":1, "Q":2, "K":3, "T":4, "A":5}
        pointValues = {"9":0, "J":0, "Q":0, "K":1, "T":1, "A":1}
        for _ in range(self.num_decks):
            for suit in self.suits:
                for denomination in self.denominations:
                    strength = strengths[denomination]
                    pointValue = pointValues[denomination]
                    self.cards.append(Card(suit, denomination, strength, pointValue))

    # Note that this doesn't reset the deck
    def shuffle(self):
        for t in range(5):
            random.shuffle(self.cards)
    
    
    def deal_card(self):
        #TODO Make deal stop with 4 cards without messing things up

        if len(self.cards) > 4:
            return self.cards.pop()
        else:
            print("Cards are dealt, 4 left in the kitty.")
            return None
    
    def deal_kitty(self):
        if len(self.cards) > 4:
            print(f"Can't add to the kitty - {len(self.cards)} in deck.")
        elif len(self.cards) <= 4 and len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("All cards dealt") 

    def __repr__(self) -> str:
        """`deck` returns card string"""
        return ' '.join(str(card) for card in self.cards)


    def __str__(self) -> str:
        """`deck.cards` returns list of card strings"""
        return ', '.join(str(card) for card in self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

class Player:
    def __init__(self, name="") -> None:
        #TODO Show hand as hand.sort() in show_hand
        self.hand = []
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

    # NOTE:
    # Can use p1 = 'Player 1'
    # p1 = Player(p1)
    # p1.name >>> 'Player 1'
    
    def add_card_to_hand(self, card):
        if isinstance(card, Card):
            self.hand.append(card)
        elif isinstance(card, list):
            self.hand.extend(card)
        else:
            print(f"add_card_to_hand failure - type {type(card)}")
    
    # NOTE Should this be split into self.cards.play and self.cards.discard?
    def remove_card_from_hand(self, card):
        return self.hand.pop(self.hand.index(card))

    def discard(self, card):
        pass


    def play_card(self, card):
        #TODO Figure out table space
        pass

    def show_hand(self):
        return sorted(self.hand)

if __name__ == "__main__":
    #print(rules)
    deck = Deck()
    game = Game()


# TODO: ensure suit is followed
# TODO: ensure higher card is played if one is available
# TODO: check winning card
# TODO: 
# TODO: 
# TODO: 
# TODO: 

# NOTE TESTING
p1 = Player('Player 1')
p2 = Player('Player 2')
p3 = Player('Player 3')
p4 = Player('Player 4')
players = [p1, p2, p3, p4]
game.deal()
a = p1.hand[0]
b = p1.hand[-1]

def _sortTest(card):
    # NOTE This may need to be split up into different fuctions
    # one for initial hand, one as an option for after trump is called
    # NOTE lead card is for calculating winning card
    # NOTE This setup was not intended for player show_hand()

    _tmp_suits = Deck.suits.copy()
    # Handle initial shuffle.  
    # TODO Raalize that you made Card.strength and unclutter this 
    game.lead_suit = \
        game.lead_suit if game.lead_suit != None else random.choice(_tmp_suits)
    game.trump_suit = \
        game.trump_suit if game.trump_suit != None else random.choice(_tmp_suits)
    suit_value = []
    suit_value.insert(0, _tmp_suits.pop(_tmp_suits.index(game.trump_suit)))
    try:
        suit_value.insert(0, _tmp_suits.pop(_tmp_suits.index(game.lead_suit)))
    except ValueError:
        pass
    finally:
        suit_value[0:0] = _tmp_suits # like extending the list at the beginning
    return card.strength + (suit_value.index(card.suit) * 10)

# TODO Should this go in the Game class?
SPADES   =  "♠"
HEARTS   =  "♥"
DIAMONDS =  "♦"
CLUBS    =  "♣"
