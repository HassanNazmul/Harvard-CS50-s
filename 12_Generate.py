"""
random - a module that contains a number of functions that can be used to generate random numbers.
choice - a function that can be used to randomly select an item from a list.
randint - a function that can be used to generate a random integer between two specified integers.
shuffle - a function that can be used to randomly shuffle the items in a list.
"""

# from random import choice
# coin = choice(["Heads", "Tails"])
# print(coin)

import random

# numer = random.randint(1, 10)
# print(numer)

card = ["Jack", "Queen", "King", "Ace"]
random.shuffle(card)
for card in card:
    print(card)