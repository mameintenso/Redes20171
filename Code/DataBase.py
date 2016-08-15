#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from Constants.Constants import *

"""
This script manages the encryption of usernames and
password and the storage of them in a file
whose name is specified in Constants/Constants.py
:author AlOrozco53, TuringOraculosLocos:
"""

def encrypt_word(word):
    """
    Encrypts word by adding ASCII_OFFSET units to each charachter's
    ascii value. Allowed characters are specified in Readme.md
    An error is raised if the word contains any character outside
    the range [ASCII_INIT, ASCII_END] (see Constants/Constants.py)
    :param word: word to encrypt
    :returns an encrypted word:
    """
    # variable to store the encrypted word
    encrypted = ''

    for letter in word:
        ascii_val = ord(letter)
        if ascii_val < ASCII_INIT or ascii_val > ASCII_END:
            # the current letter is invalid!
            raise IndexError('The current ascii value is out of the range '\
                             + '[' + str(ASCII_INIT) + ', '\
                             + str(ASCII_END) + ']')
        else:
            ascii_val -= ASCII_INIT
            new_val = ((ascii_val + ASCII_OFFSET) % ASCII_LEN) + ASCII_INIT
            encrypted += chr(new_val)
    return encrypted

def decrypt_word(word):
    """
    Decrypts word by subtracting ASCII_OFFSET units to each charachter's
    ascii value. Allowed characters are specified in Readme.md
    An error is raised if the word contains any character outside
    the range [ASCII_INIT, ASCII_END] (see Constants/Constants.py)
    :param word: word to decrypt
    :returns a decrypted word:
    """
    # variable to store the decrypted word
    decrypted = ''

    for letter in word:
        ascii_val = ord(letter)
        if ascii_val < ASCII_INIT or ascii_val > ASCII_END:
            # the current letter is invalid!
            raise IndexError('The current ascii value is out of the range '\
                             + '[' + str(ASCII_INIT) + ', '\
                             + str(ASCII_END) + ']')
        else:
            ascii_val -= ASCII_INIT
            new_val = ((ascii_val - ASCII_OFFSET) % ASCII_LEN) + ASCII_INIT
            decrypted += chr(new_val)
    return decrypted

def decrypt_file():
    """
    Decrypts the file that stores all the usernames and passwords.
    See Readme.md for more information on the format of the database file.
    :returns a dictionary with decrypted usernames as keys and decrypted
    passwords as values:
    """
    # variable to store the decrypted file
    database = {}

    with open(DATABASE_PATH, 'r') as dbfile:
        for line in dbfile:
            pair = line.strip().split(' ')
            key = decrypt_word(pair[0])
            value = decrypt_word(pair[1])
            database[key] = value
    return database

def encrypt_file(database):
    """
    Encrypts the dict database and writes it in
    the file that stores all the usernames and passwords.
    See Readme.md for more information on the format of the database file.
    If the file doesn't exist, it is created.
    :param database to encrypt:
    """
    # if the database file does not exists, a new one is creating
    # storing the admin's credentials
    if not os.path.isfile(DATABASE_PATH):
        with open(DATABASE_PATH, 'w+') as dbfile:
            dbfile.write(ADMIN_USERNAME + ' ' + ADMIN_PASSWORD)

    # store all credentials in database
    with open(DATABASE_PATH, 'w+') as dbfile:
        string = ''
        for key, value in database.items():
            string += encrypt_word(key) + ' ' + encrypt_word(value) + '\n'
        dbfile.write(string.strip())
