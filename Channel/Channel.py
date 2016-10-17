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
import xmlrpclib


"""
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
"""
class Channel:

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
        self.api_server = MyApiServer(self.my_ip, self.my_port, gui)
        self.api_client = MyApiClient(self.proxy_uri)

        # start server
        self.api_server.start()

        # audio and video buffers
        self.queue = mp.Queue()
        self.vqueue = mp.Queue()

        # for recording audio and sending it
        self.audio_rec = AudioRecorder()

        # video recorder
        self.video_rec = VideoRecorder(self.vqueue, self.api_client)


    def send_text(self, text):
        """
        Metodo que se encarga de mandar texto al contacto con
        el cual se estableció la conexión
        """
        print self.api_client.send_message(text)

    def start_audio_call(self, calling):
        self.thr = Thread(target=self.audio_rec.run,
                     args=(self.queue, calling, ))
        self.thr.start()
        self.api_client.receive_call(calling)
        while calling:
            print 'calling: ' + str(calling)
            audio_chunk = self.queue.get()
            data = xmlrpclib.Binary(audio_chunk.tobytes())
            self.api_client.play_audio(data)

    def stop_audio_call(self):
        if self.audio_rec.is_alive():
            self.audio_rec.terminate()

    def start_video_call(self):
        self.video_rec.setDaemon(True)
        self.video_rec.start()
