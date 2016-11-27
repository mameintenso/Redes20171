#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import sys
from Constants.Constants import CHAT_PORT
from Constants.AuxiliarFunctions import *
from Channel.Channels import *

class MyApiClient:

    def __init__(self, contact_ip=None, contact_port=None):
        if contact_port:
            self.proxy_uri = 'http://localhost:' + str(contact_port)
        elif contact_ip:
            self.proxy_uri = 'http://' + contact_ip + ':' + str(CHAT_PORT)
        else:
            raise ValueError('The values of fields are not consistent MyApiClient.__init__')
        self.server = xmlrpclib.ServerProxy(self.proxy_uri, allow_none=True)

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

    def get_contacts(self, username):
        return self.server.get_contacts_wrapper(str(username))

    def connect_contact(self, ip, port, username):
        self.server.connect_wrapper(str(ip), str(port), str(username))

    def disconnect_contact(self, username):
        self.server.disconnect_wrapper(str(username))

    def opengui(self, receiving_name, receiving_ip, receiving_port):
        print 'receiving_name: ' + str(receiving_name)
        self.server.new_chat_wrapper(receiving_name, receiving_ip, receiving_port)
