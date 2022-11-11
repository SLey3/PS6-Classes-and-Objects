# File: card.py
# Name: Sergio Ley Languren

"""This file defines the Card class, which represents a playing card."""
# imports
from enum import Enum
from typing import Union, Optional


# Card and Rank Enums
class CardSuites(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

class SpecialRank(Enum):
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

# ----------------------------------------------------

def _convert_str_to_list(string: str) -> list:
    integer = "" # rank 
    li = []
    for ch in string:
        try:
            if int(ch): # if character can be turned into an int type then it is a rank rather than a suite type
                integer += ch
        except ValueError: # character is not a int so it can either be a suite type or a special rank
            li.append(ch)
    li.insert(0, int(integer))
    return li


class Card:
    """The Card class represents a playing card as a rank-suit pair."""
    def __init__(self, rank: Union[int, SpecialRank, str], suite: Optional[CardSuites] = None):
        self.rank = rank
        if not isinstance(rank, str) and suite is not None:
            self.suite = suite.name[:-(len(suite.name) - 1)] # string splicing to only get the first character
        self._check_rank()


    def _check_with_suite(self):
        # two seperate checks will be made depending on the instance of self.rank
        # 1) if self.rank is the instance of the SpecialRank enum
        if isinstance(self.rank, SpecialRank):
            self.rank = self.rank.name[:-(len(self.rank.name) - 1)]
        else:
            # 2) if self.rank is an integer, then this check will check if the integer matches one of the values
            # within the attributes of SpecialRank
            for special in SpecialRank:
                if self.rank == special.value: # checks if self.rank matches the current iterated special rank
                    self.rank = special.name[:-(len(special.name) -1)]

    def _check_without_suite(self):
        li = _convert_str_to_list(self.rank) # turn into list for clearer values
        for special in SpecialRank: # identical to _check_with_suite for loop
            if li[0] == special.value: # except li[0] is the rank and thus checks if the rank is equal to the value of the current iterated special rank
                li[0] = special.name[:-(len(special.name) - 1)]
        
        self.rank = f"{li[0]}"
        self.suite = li[1]

    def _check_rank(self):
        if isinstance(self.rank, str):
            # If self.rank is a string the self.suite is not defined yet and must be defined thus check_without_suite
            self._check_without_suite()
        else:
            # if self.rank is either int or SpecialRank type and thus self.suite is defined
            self._check_with_suite()

    def get_rank(self):
        """gets the cards rank"""
        return self.rank

    def get_suite(self):
        """gets the cards suite type"""
        return self.suite

    def __str__(self):
        return f"{self.rank}{self.suite}"

def test_card_class():
    """Prints every card in a 52-card deck, one suit per line."""
    card_in_suite = 13
    suites = [CardSuites.CLUBS, CardSuites.DIAMONDS, CardSuites.HEARTS, CardSuites.SPADES]

    for s in suites:
        for i in range(1, card_in_suite + 1):
            print(Card(i, s), "\t", sep=",", end="") # overrriding setting newline default so I can do it manually when going to the next suite
        print("\n")

# Startup code

if __name__ == "__main__":
    test_card_class()
