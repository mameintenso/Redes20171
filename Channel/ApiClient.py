#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import sys
sys.path.insert(0, '../Constants')
from Constants import CHAT_PORT
from AuxiliarFunctions import *

class MyApiClient:

    def __init__(self, contact_ip = None, contact_port = None):
        if contact_port:
            #TODO
        elif contact_ip:
            #TODO
        else:
            raise ValueError('The values of fields are not consistent MyApiClient.__init__')

    def send_message(self, message):
        print(self.server.sendMessage_wrapper(str(message)))

    def stop_audio_call(self):
        print(self.server.stopAudio_wrapper())

    def play_audio(self, audio):
        print(self.server.playAudio_wrapper(audio))

    def play_video(self, data):
        print(self.server.playVideo_wrapper(data))

    def stop_video(self):
        try:
            print(self.server.stopVideo_wrapper())
        except:
            print(self.server.stopVideo_wrapper())
