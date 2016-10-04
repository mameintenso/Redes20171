#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:Funciones auxiliares                      #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
from __future__ import absolute_import

import socket

"""**************************************************
 Metodo auxiliar que hace uso de internet para
 conocer la ip con la que contamos como usuarios
**************************************************"""

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return "%s"% (s.getsockname()[0])

"""**************************************************
 Clase auxiliar que implementa el metodo
stop, para que el hilo se detenga externamente
**************************************************"""

import threading

class MyThread(threading.Thread):

    def __init__(self, target, args):
        super(MyThread, self).__init__(target=target, args=args)
        self._stop = threading.Event()
        self.target = target
        self.args = args

    def stop(self):
        self._stop.set()

    def is_stop(self):
        return self._stop.isSet()

    def run(self):
        self.target(self.args[0])
        while not self.is_stop():
            pass

    def join(self, timeout=None):
        self._stop.set()
        threading.Thread.join(self, timeout)
