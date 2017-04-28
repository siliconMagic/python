#! /usr/bin/python
'''
module docstring
'''

import random

def to_weird_case(string):
    '''
    function docstring
    '''

    weird_words = []
    for word in string.split():
        weird = ''
        for i, letter in enumerate(word):
            if i % 2 == 0:
                weird += letter.upper()
            else:
                weird += letter.lower()
        weird_words.append(weird)
    return ' '.join(weird_words)

print(to_weird_case('This is a test.'))

def a_new_magic_function():
    '''
    function docstring
    '''

    print(random.randint(1, 10))

a_new_magic_function()
