#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from Channel.ApiClient import *
from Channel.ApiServer import *
from Channel.RecordAudio import *
from Channel.RecordVideo import *
from Constants.AuxiliarFunctions import *

import multiprocessing as mp
from threading import Thread


"""
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
"""
class RequestChannel:

    def __init__(self, local_ip, local_port, contact_ip, contact_port, gui):
        """
        Constructor de la clase
        @param <str> contact_ip: Si no se trabaja de manera local
        representa la ip del contacto con el que se
        establecera la conexion
        @param <int> my_port: De trabajar de manera local puerto
        de la instancia del cliente
        @param <int> contact_port: De trabajar de manera local
        representa el puerto de la instancia del contacto
        """
        self.proxy_uri = 'http://' + contact_ip + ':' + contact_port
        self.my_ip = local_ip
        self.my_port = local_port
        self.gui = gui
        self.api_server = MyApiServer(self.my_ip, self.my_port, gui)
        self.api_client = MyApiClient(self.proxy_uri)

        # start server
        self.api_server.setDaemon(True)
        self.api_server.start()

        # audio and video buffers
        self.queue = mp.Queue()
        self.vqueue = mp.Queue()

        # for recording audio and sending it
        self.audio_rec = AudioRecorder(self.api_client, self.queue)

        # video recorder
        self.video_rec = VideoRecorder(self.api_client)



    """**************************************************
    Metodo que se encarga de mandar iniciar una conversacion
    con un nuevo contacto
    **************************************************"""
    def new_connection(self, my_ip, my_port):
        #TODO

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

class BidirectionalChannel(RequestChannel):

    def __init__(self, Qparent, contact_ip = None,  contact_port = None,my_port = None):
        if my_port and contact_port:
            #El objeto api server necesita correr en un hilo aparte
            #TODO
        elif contact_ip:
            #TODO
        else:
            raise ValueError('The values of fields are not consistent BidirectionalChannel.__init__')
        #TODO

    """**************************************************
    Metodos Get
    **************************************************"""
    def get_api_server(self):
        return self.api_server_thread
