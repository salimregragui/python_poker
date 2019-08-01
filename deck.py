"""
Deck and cards module
"""
from random import shuffle

class Card:
    """Card class"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    """Deck class"""
    def __init__(self):
        suits = ["Hearths", "Diamonds", "Clubs", "Spades"]
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def deck_restart(self):
        suits = ["Hearths", "Diamonds", "Clubs", "Spades"]
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def shuffle_deck(self):
        shuffle(self.cards)
