#!/usr/bin/env python3

import pdb
import random

game_rules = """ 
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

meld_rules = """
    run      	    A-10-K-Q-J of trump 	                        15
    aces 	        four aces, one of each suit 	                10
    kings       	four kings, one of each suit 	                8
    queens 	        four queens, one of each suit 	                6
    jacks 	        four jacks, one of each suit 	                4
    pinochle     	queen of spades and jack of diamonds 	        4
    double pinochle queen of spades and jack of diamonds 	        30
    triple pinochle queen of spades and jack of diamonds 	        60
    royal marriage 	K-Q of trump (unless in a run)* 	            4
    common marriage	K-Q of nontrump suit                            2
    dix 	        9 of trump 	                                    1
    double run 	    both sequences A-10-K-Q-J of trump 	            40
    double aces 	two aces of every suit                        	100
    double kings 	two kings of every suit                        	80
    double queens 	two queens of every suit                        60
    double jacks 	two jacks of every suit                         40
    double pinochle	two queens of spades and jacks of diamonds 	    30 
    triple aces 	three aces of every suit                       	150
    triple kings 	three kings of every suit                      	120
    triple queens 	three queens of every suit                      90
    triple jacks 	three jacks of every suit                       60
    triple pinochle	three queens of spades and jacks of diamonds 	60 
    # NOTE that a run should not also include to points of a marriage
"""

class Card:

    DENOMINATIONS = ["9", "J", "Q", "K", "T", "A"] # NOTE used T for 10
    SUITS = ["♦", "♣", "♥", "♠"] # Digraph is cC cD cH cS

    def __init__(self: 'Card', suit: str, denomination: str, strength: int, pointValue: int) -> None:
        self.suit = suit
        self.denomination = denomination
        self.strength = strength
        self.pointValue = pointValue

    def __str__(self: 'Card') -> str:
        return f"{self.denomination}{self.suit}"

    def name(self: 'Card') -> str:
        # NOTE ANSI escape char (\033) does NOT count towards string length
        terminal_colors = "\033[30m\033[47m" if self.suit in ["♣", "♠"] else \
                ("\033[31m\033[47m" if self.suit in ["♦", "♥"] else "\033[30m")
        return f"{terminal_colors}{self.denomination}{self.suit}\033[0m"
        # str(Card)[10:12] gives the denomination and suit as one string
        # `d, s = str(Card)[10:12]` gives the denomination and suit seperately

    def __repr__(self: 'Card') -> str:
        # NOTE ANSI escape char (\033) does NOT count towards string length
        terminal_colors = "\033[30m\033[47m" if self.suit in ["♣", "♠"] else \
                ("\033[31m\033[47m" if self.suit in ["♦", "♥"] else "\033[30m")
        return f"{terminal_colors}{self.denomination}{self.suit}\033[0m"
    
    def _compare(self: 'Card', other: 'Card', trump_suit: str = None) -> str:
        # Note: We don't need a lead_suit passed in, as the lead suit will not compare 
        #   against anything, and the high card will either be lead suit or trump suit
        # TODO make sure there is a top card or winning card that can be passed as "other"
        #self_suit_i = 
        if trump_suit == None:
            if game.trump_suit != None:
                trump_suit = game.trump_suit
        if other.suit == trump_suit:
            if self.suit != trump_suit:
                return 'lt'
            if self.strength > other.strength:
                return 'gt'
            return 'lt'
        if self.suit == trump_suit:
            return 'gt'
        if self.suit != other.suit:
            return 'lt'
        if self.strength > other.strength:
            return 'gt'
        if self.name == other.name:
            return 'eq'
        return 'lt'



    def value(self: 'Card') -> int:
        return int(self.pointValue)
     
    def strength(self: 'Card') -> int:
        return int(self.strength)

    def suit(self: 'Card') -> str:
        return self.suit

    def __gt__(self: 'Card', other: 'Card') -> int:
        return self._compare(other) == 'gt'
    
    def __lt__(self: 'Card', other: 'Card') -> int:
        return self._compare(other) == 'lt'
        #return str(self) > str(other)
#        if game.trump_suit != None:
#            _suits = Deck.suits.copy()
#        else:
#            _suits = Deck.suits.copy()[Deck.suits.index(game.trump_suit):] + \
#                    Deck.suits.copy()[:Deck.suits.index(game.trump_suit)]
#        return str(_suits.index(self.suit)) + str(self.strength) <  \
#                str(_suits.index(other.suit)) + str(other.strength)

    def __eq__(self: 'Card', other: 'Card') -> bool:
        return self._compare(other) == 'eq'
#        if game.trump_suit != None:
#            _suits = Deck.suits[Deck.suits.index(game.trump_suit):] + \
#                    Deck.suits[:Deck.suits.index(game.trump_suit)]
#        else:
#            _suits = Deck.suits.copy()
#        return str(_suits.index(self.suit)) + str(self.strength) ==  \
#                str(_suits.index(other.suit)) + str(other.strength)

    
# TODO: Make deck part of Game class and initialize on start.
# TODO: Make shuffle part of a new hand method.
class Game:
    def __init__(self: 'Game', num_players: int=4) -> None:
        self.deck = Deck()
        self.players = [Player(f'Player {i+1}') for i in range(num_players)]
        # NOTE If number of players is below 4, add Bot to prevent bugs
        # Or just leave it as is and figure out a system for AI players?
        self.current_bid = 40
        self.bid_winner = None
        #TODO Add game.bid_winner assignment 
        self.kitty = []
        self.trump_suit = None
        self.lead_suit = None
        self.dealer = self.players[-1] # new hand changes dealer first
        self.current_player = self.dealer
        # NOTE Should this be a defined method with players and points?  Or part
        # of the Player class?
        self.team1 = self.players[0::2]
        self.team2 = self.players[1::2]
        self.t1_score = 0
        self.t2_score = 0
    # __getitem__(self, key) is used to evaluate self[key]
    # calling my_obj[key] will evaluate my_obj.__getitem__(key)
    # NOTE use Game[player_name] and NOT Game.players[]

    def __getitem__(self: 'Game', player_name: str) -> str:
        for player in self.players:
            if player.name == player_name:
                return player
        raise KeyError(f"No player with the name '{player_name}'")

    def new_hand(self: 'Game') -> None:
        """A round consists of six phases: dealing, bidding, exchanging, melding
        trick taking, and scoring"""
        # Switch dealer # Initial dealer set to player 4
        self.change_dealer()
        # shuffle and deal cards
        self.deal()  
        # start bidding
        # bid winner or throw in hand
            # if bid winner, add kitty and discard
                # play round until no more cards
            # if throw in hand, new hand


    def deal(self: 'Game') -> None:
        self.kitty = []
        self.deck.shuffle()
        while len(self.deck.cards) > 4:
            for player in self.players:
                player.hand.append(self.deck.cards.pop(0))
        self.kitty.extend(\
            [self.deck.cards.pop(0) for i in range(len(self.deck.cards))])
        for player in players:
            player.hand.sort()

    def change_dealer(self: 'Game') -> None:
        current_dealer_index = self.players.index(self.dealer)
        self.dealer = self.players[(current_dealer_index+1) % len(self.players)]
#        if self.players[current_dealer_index] != self.players[-1]:
#            self.dealer = self.players[current_dealer_index+1]
#        else:
#            self.dealer = players[0]

    def score(self: 'Game') -> int:
        self.t1_score += sum(player.score for player in self.team1)
        self.t2_score += sum(player.score for player in self.team2)
        print(f"{self.team1 = }, scores is: \n") # add right just space filled score  
        print(f"{self.team2 = }, scores is: \n") # add right just space filled score  
        pass

    def start_bidding(self: 'Game') -> None:
        if self.dealer == self.current_player:
            self.change_dealer()
        keep_going = True
        print(f"{self.dealer} dealt, {self.current_player} will start the bidding") 
        #TODO ensure that self.bid_winner is reset to None after round ends
        while keep_going:
            # This is a mess
            # we need to ask the player, get an answer and do something with the answer:w
            
            self.current_player.bid()

    def next_player(self: 'Game') -> None:
        current_player_index = self.players.index(self.current_player)
        self.current_player = self.players[(current_dealer_index+1) % len(self.players)]

    def _show_hands(self: 'Game') -> list[list]:
        for player in self.players:
            print(player.show_hand())


    def play(self: 'Game') -> None:
        # deal
        self.new_hand()
        # bid
        # name trump
        # meld
        # discard
        # while cards, play hand
        pass


class Deck:
    denominations = ["9", "J", "Q", "K", "T", "A"] # NOTE used T for 10
    suits = ["♦", "♣", "♥", "♠"] # Digraph is cC cD cH cS

    def __init__(self: 'Deck', num_decks=3) -> None:
        self.num_decks = num_decks
        self.cards = []
        self.create_deck()
    
    def create_deck(self: 'Deck') -> None:
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
    def shuffle(self: 'Deck') -> None:
        for t in range(5):
            random.shuffle(self.cards)
    
    
    def deal_card(self: 'Deck') -> None:
        #TODO Make deal stop with 4 cards without messing things up

        if len(self.cards) > 4:
            return self.cards.pop()
        else:
            print("Cards are dealt, 4 left in the kitty.")
            return None
    
    def deal_kitty(self: 'Deck') -> None:
        """4 cards that are bid on"""
        if len(self.cards) > 4:
            print(f"Can't add to the kitty - {len(self.cards)} in deck.")
        elif len(self.cards) <= 4 and len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("All cards dealt") 

    def __repr__(self: 'Deck') -> str:
        """`deck` returns card string"""
        return ' '.join(str(card) for card in self.cards)


    def __str__(self: 'Deck') -> str:
        """`deck.cards` returns list of card strings"""
        return ', '.join(str(card) for card in self.cards)

    def __len__(self: 'Deck') -> int:
        return len(self.cards)

    def __getitem__(self: 'Deck', position: int) -> str:
        return self.cards[position]

class Player:
    def __init__(self: 'Player', name: str ="") -> None:
        #TODO Show hand as hand.sort() in show_hand
        self.hand = []
        self.name = name
        self.score = 0 # Use as current hand score, not total score
    
    def __repr__(self: 'Player') -> str:
        return self.name

    # NOTE:
    # Can use p1 = 'Player 1'
    # p1 = Player(p1)
    # p1.name >>> 'Player 1'
    
    def add_card_to_hand(self: 'Player', card: 'Card') -> None:
        if isinstance(card, Card):
            self.hand.append(card)
        elif isinstance(card, list):
            self.hand.extend(card)
        else:
            print(f"add_card_to_hand failure - type {type(card)}")
    
    # NOTE Should this be split into self.cards.play and self.cards.discard?
    def discard(self: 'Player', card: 'Card') -> None:
        """Discard after winning the kitty"""
        return self.hand.pop(self.hand.index(card))

    def _is_suit_playable(self: 'Player', card: 'Card') -> None:
        if game.lead_suit == None:
            return True
        if game.lead_suit == game.trump_suit: #and #TODO add current round winning card
            pass
        # TODO
         

    def play_card(self: 'Player', card: 'Card') -> None:
        # TODO create check if card is playable
    
        #TODO Figure out table space


        # Check that player has card
        # select card
        # remove card from hand
        # Tell the table that player played card / put on table
        # return card?


        pass

    def bid(self: 'Player') -> None:
        ans = input(f"Please enter {Game.current_bid + 1} or higher, or press [P/p/0] to pass")
        if ans.lower == 'p' or ans == '0':
            return 0
        elif int(ans) > Game.current_bid:
            return int(ans)
        elif int(ans) <= Game.current_bid:
            print("Your bid must be higher than the current bid")
            self.bid()
        else:
            self.bid()

    def show_hand(self: 'Player') -> list:
        """Show the player their hand"""
        return sorted(self.hand)


if __name__ == "__main__":
    #print(game_rules)
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
# NOTE Could this be created in the new game without making it directly a game object
p1 = Player('Player 1')
p2 = Player('Player 2')
p3 = Player('Player 3')
p4 = Player('Player 4')
players = [p1, p2, p3, p4]
#game.deal()
game.play()
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


