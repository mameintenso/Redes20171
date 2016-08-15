#!/usr/bin/python
# -*- coding: utf-8 -*-

from Code.DataBase import *
from Code.Calculator import *

"""
Main script for Practica1
:author AlOrozco53, TuringOraculosLocos:
"""


def main():
    # provisional code to test the functionality of the program
    # DELETE THIS SHIT
    calc = AdvancedCalculator()
    inp = ''
    while True:
        print('curr screen:', calc.curr_screen,
              'prev screen:', calc.prev_screen,
              'operator:', calc.operator,
              '\n', '-------------------------')
        inp = input()
        if inp in ['/', '*', '+', '-', '=']:
            calc.enter_op(inp)
        else:
            calc.enter_digit(inp)


if __name__ == '__main__':
    main()
