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

class Card:
    def __init__(self, suit, denomination, strength, pointValue) -> None:
        self.suit = suit
        self.denomination = denomination
        self.strength = strength
        self.pointValue = pointValue

    def __str__(self) -> str:
        return f"{self.denomination}{self.suit}"

    def __repr__(self) -> str:
        return f"{self.denomination}{self.suit}"
    
    def value(self):
        return int(self.pointValue)
     
    def strength(self):
        return int(self.strength)
    
# TODO: Make deck part of Game class and initialize on start.
# TODO: Make shuffle part of a new hand method.
class Game:
    def __init__(self) -> None:
        pass

class Deck:
    def __init__(self, num_decks=3) -> None:
        self.num_decks = num_decks
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        suits = ["♣", "♢", "♡", "♠"] # Digraph is cC cD cH cS
        # TODO Add terminal colors - red and black - with background white
        denominations = ["9", "J", "Q", "K", "T", "A"] # NOTE used T instead of 10
        strengths = {"9":0, "J":1, "Q":2, "K":3, "T":4, "A":5}
        pointValues = {"9":0, "J":0, "Q":0, "K":1, "T":1, "A":1}
        for _ in range(self.num_decks):
            for suit in suits:
                for denomination in denominations:
                    strength = strengths[denomination]
                    pointValue = pointValues[denomination]
                    self.cards.append(Card(suit, denomination, strength, pointValue))

    # Note that this doesn't reset the deck
    def shuffle(self):
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

class Player:
    def __init__(self, name="") -> None:
        self.hand = []
        self.name = name

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
        return self.cards.pop(card) 

    def play_card(self, card):
        #TODO Figure out table space
        pass

if __name__ == "__main__":
    #print(rules)
    deck = Deck()
    #deck.shuffle()


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