#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from Channel.ApiClient import *
from Channel.ApiServer import *
from Channel.RecordAudio import *
from Channel.RecordVideo import *
from Constants.AuxiliarFunctions import *
from Constants.Constants import *

import multiprocessing as mp
from threading import Thread


"""
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
"""
class RequestChannel(object):
    """**************************************************
    Convencion: Si trabajamos de manera local, entonces
    haremos uso de los campos de contact_port y my_port
    por lo que el campo de contact_ip puede ser nulo.
    Si trabajamos con instancias en la red solo se hara uso
    del campo de contact_ip
    **************************************************"""

    def __init__(self, Qparent, my_port, contact_ip=None,
                 contact_port=None, server=None, my_name=None):
        """**************************************************
        Constructor de la clase
        @param <str> contact_ip: Si no se trabaja de manera local
        representa la ip del contacto con el que se
        establecera la conexion
        @param <int> my_port: De trabajar de manera local puerto
        de la instancia del cliente
        @param <int> contact_port: De trabajar de manera local
        representa el puerto de la instancia del contacto
        **************************************************"""
        if my_port and contact_port:
            self.my_ip = 'localhost'
            self.api_client = MyApiClient(contact_port=contact_port)
        else:
            self.my_ip = get_ip_address()
            self.api_client = MyApiClient(contact_ip=contact_ip)
        self.my_port = my_port
        self.gui = Qparent
        if server is None:
            self.api_server = MyApiServer(self.my_ip, self.my_port,
                                          self.gui, my_name)
            # start server
            self.api_server.setDaemon(True)
            self.api_server.start()
        else:
            self.api_server = server

    def new_connection(self, my_name):
        """**************************************************
        Metodo que se encarga de mandar iniciar una conversacion
        con un nuevo contacto
        **************************************************"""
        self.my_name = my_name

        # audio and video buffers
        self.queue = mp.Queue()
        self.vqueue = mp.Queue()

        # for recording audio and sending it
        self.audio_rec = AudioRecorder(self.api_client, self.queue)

        # video recorder
        self.video_rec = VideoRecorder(self.api_client)

    def send_text(self, text):
        """
        Metodo que se encarga de mandar texto al contacto con
        el cual se estableció la conexión
        """
        print self.api_client.send_message(text)

    def start_video_call(self):
        self.video_rec.setDaemon(True)
        self.video_rec.start()
        return self.video_rec

    def start_audio_call(self):
        # thread that records audio
        self.audio_rec.setDaemon(True)
        self.audio_rec.start()

        # thread that plays audio
        self.playing_thread = Thread(target=self.audio_rec.play_audio)
        self.playing_thread.setDaemon(True)
        self.playing_thread.start()
        return self.audio_rec

    def open_friend_gui(self):
        self.friendgui = Thread(target=self.api_client.opengui,
                                args=(self.my_ip, self.my_port, self.my_name))
        self.friendgui.setDaemon(True)
        self.friendgui.start()

    """**************************************************
    Metodos Get
    **************************************************"""
    def get_api_server(self):
        return self.api_server


class BidirectionalChannel(RequestChannel):

    def __init__(self, Qparent, contact_ip=None, contact_port=None,
                 my_port=None, my_name=None):
        if my_port and contact_port:
            super(BidirectionalChannel, self).__init__(Qparent=Qparent,
                                                       my_port=my_port,
                                                       contact_port=contact_port,
                                                       my_name=my_name)
        elif contact_ip:
            super(BidirectionalChannel, self).__init__(Qparent=Qparent,
                                                       myport=my_port,
                                                       contact_ip=contact_ip,
                                                       my_name=my_name)
        else:
            raise ValueError('The values of fields are not consistent BidirectionalChannel.__init__')
        self.gui = Qparent

        # # start server thread
        # self.api_server.setDaemon(True)
        # self.api_server.start()

    """**************************************************
    Metodos Get
    **************************************************"""
    def get_api_server(self):
        return self.api_server
