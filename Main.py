#!/usr/bin/python
# -*- coding: utf-8 -*-

from Code.DataBase import *
from Code.Calculator import *
from GUI.MainGui import *
from GUI.CalcGui import *

"""
Main script for Practica1
:author AlOrozco53, TuringOraculosLocos:
"""


def main():
    # if the database file does not exists, a new one is created
    # storing the admin's credentials
    if not os.path.isfile(DATABASE_PATH):
        with open(DATABASE_PATH, 'w+') as dbfile:
            dbfile.write(encrypt_word(ADMIN_USERNAME)\
                         + ' '\
                         + encrypt_word(ADMIN_PASSWORD))

    # if the database file does not have the admin's credentials,
    # we add them
    db = decrypt_file()
    if not (ADMIN_USERNAME in db.keys() and\
            ADMIN_PASSWORD ==  db[ADMIN_USERNAME]):
        db[ADMIN_USERNAME] = ADMIN_PASSWORD
        encrypt_file(db)

    app1 = QtGui.QApplication(sys.argv)
    welcome_window = Welcome()

    sys.exit(app1.exec_())

    # app2 = QtGui.QApplication(sys.argv)
    # calc_window = CalcGui()

    # sys.exit(app2.exec_())


if __name__ == '__main__':
    main()
