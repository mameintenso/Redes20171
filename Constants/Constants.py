#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This script stores all the constants used
by the rest of the scripts, as a means of
maintaining ellegance throughout the source code.
:author AlOrozco53, TuringOraculosLocos:
"""

# number of units to be used as encryption offset
ASCII_OFFSET = 5

# index of the first character in the ascii
# alphabet allowed to be in a username and/or password
ASCII_INIT = 33

# index of the last character in the ascii
# alphabet allowed to be in a username and/or password
ASCII_END = 126

# length of the actual ascii subalphabet allowed to
# build a username and/or password
ASCII_LEN = 93

# username/password database filename
DATABASE_PATH = 'Code/Input.txt'

# default username for the admin user
ADMIN_USERNAME= 'root'

# default password for the admin user
ADMIN_PASSWORD = 'root'

# variables that store features for all the GUIs
LOGIN_WIDTH = 500
LOGIN_HEIGTH = 400
DEFAULT_POSTION_X = 350
DEFAULT_POSTION_Y = 350
