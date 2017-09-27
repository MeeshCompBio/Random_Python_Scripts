import collections
from random import choice

# This represents a class using a named tuple
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # This populatied the deck with each suit number combo
        # list comprehension
        self.cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        # return the lenght of the class
        return len(self._cards)

        # Get item automatically support slicing
    def __getitem__(self, position):
        # allows indexing for the class
        return self._cards[position]


# Commands to try in an interactive terminal
beer_card = Card('7', 'diamonds')
beer_card
deck = FrenchDeck()
len(deck)
# We can index our class
deck[0]
# Even select a random card
choice(deck)
# sliceing the dataset
deck[12::13]

# we can also iterate through it
for card in deck:
    print(card)

# We can check to see if card are in deck since it is iterable
Card('Q', 'hearts') in deck

# Ways to sort our cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
