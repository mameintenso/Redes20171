#!/usr/bin/python
# -*- coding: utf-8 -*-

import ..Constants.Constants

def encrypt_pass(word):
    """
    Encrypts word by adding 3 units to each charachter's
    ascii value. Allowed characters are specified in Readme.md
    An error is raised if the word contains any character outside
    the range [ASCII_INIT, ASCII_END] (see Constants/Constants.py)
    :param word: word to encrypt
    :returns an encrypted word:
    """
    # variable to store the encrypted word
    encrypted = ''

    for letter in word:
        ascii_val = char(letter)
        if ascii_val < ASCII_INIT or ascii_val > ASCII_END:
            # the current letter is invalid!
            raise IndexError('The current ascii value is out of the range'\
                             + '[' + str(ASCII_INIT)\
                             + str(ASCII_END) + ']')
        else:
            ascii_val -= ASCII_INIT
            new_val = ((ascii_val + 3) % ASCII_LEN) + ASCII_INIT
            encrypted += ord(new_val)

    return encrypted
