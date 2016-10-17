#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pyaudio
import numpy as np
import xmlrpclib

from threading import Thread
from Constants.Constants import *


class AudioRecorder(Thread):
    def __init__(self, client, queue):
        super(AudioRecorder, self).__init__()
        self.p = pyaudio.PyAudio()
        self.client = client
        self.recording = True
        self.queue = queue

    def run(self):
        '''
        Records audio and saves it in the given
        queue (buffer)
        '''
        FORMAT = self.p.get_format_from_width(2)
        stream = self.p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print 'recording audio....'
        self.recording = True
        while self.recording:
            frame = []
            for _ in range(int(RATE/CHUNK * RECORD_SECONDS)):
                frame.append(stream.read(CHUNK))
            data_ar = np.fromstring(''.join(frame),
                                    dtype=np.uint8)
            self.queue.put(data_ar)

    def play_audio(self):
        while self.recording:
            audio_chunk = self.queue.get()
            data = xmlrpclib.Binary(audio_chunk.tobytes())
            self.client.play_audio(data)

    def stop_call(self):
        self.recording = False
        try:
            self.client.stop_audio_call()
        except:
            self.client.stop_audio_call()
        print 'audio call ended by the user'
