#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pyaudio
import numpy as np

from threading import Thread

from Constants.Constants import *


class AudioRecorder(Thread):
    def __init__(self, queue):
        super(AudioRecorder, self).__init__()

        self.p = pyaudio.PyAudio()
        self.queue = queue

    def run(self):
        '''
        Records audio and saves it in the given
        queue (buffer)
        '''
        form = self.p.get_format_from_width(2)
        stream = self.p.open(format=form,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print 'recording audio....'
        while True:
            frame = []
            for _ in range(int(RATE/CHUNK * RECORD_SECONDS)):
                r = stream.read(CHUNK)
                frame.append(r)
            data_ar = np.fromstring(''.join(str(frame)),
                                    dtype=np.uint8)
            self.queue.put(data_ar)
