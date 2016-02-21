# -*- coding: utf-8 -*-
"""A simple text-based game of hangman
A re-implementation of Hangman 3-liner in more idiomatic Python 3
Original: http://danverbraganza.com/writings/hangman-in-3-lines-of-python
Requirements:
  A dictionary file at /usr/share/dict/words
Usage:
  $ python hangman.py 
Released under the MIT License. (Re)written by Arun Ravindran http://arunrocks.com
"""

import random

DICT = '/usr/share/dict/words'
chosen_word = random.choice(open(DICT).readlines()).upper().strip()
guesses = set()
scaffold = """
|======
|   |
| {3} {0} {5}
|  {2}{1}{4}
|  {6} {7}
|  {8} {9}
|
"""
man = list('OT-\\-//\\||')
guesses_left = len(man)

while not guesses.issuperset(chosen_word) and guesses_left:
    print("{} ({} guesses left)".format(','.join(sorted(guesses)), guesses_left))
    print(scaffold.format(*(man[:-guesses_left] + [' '] * guesses_left)))
    print(' '.join(letter if letter in guesses else '_' for letter in chosen_word))
    guesses.update(c.upper() for c in input() if str.isalpha(c))
    guesses_left = max(len(man) - len(guesses - set(chosen_word)), 0)

if guesses_left > 0:
    print("You win!")
else:
    print("You lose!\n{}\nHANGED!".format(scaffold.format(*man)))
print("Word was", chosen_word)
