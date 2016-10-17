#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import xmlrpclib

class MyApiClient:

    def __init__(self, proxy_uri):
        if proxy_uri is not None:
            self.server = xmlrpclib.ServerProxy(proxy_uri,
                                                allow_none=True)

    def send_message(self, message):
        print(self.server.sendMessage_wrapper(str(message)))

    def stop_audio_call(self):
        print(self.server.stopAudio_wrapper())

    def play_audio(self, audio):
        print(self.server.playAudio_wrapper(audio))
