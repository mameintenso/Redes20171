#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pyaudio
import numpy as np

from Constants.Constants import *


class AudioRecorder():
    def __init__(self):
        self.p = pyaudio.PyAudio()

    def run(self, queue, calling):
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
        while calling:
            frame = []
            for _ in range(int(RATE/CHUNK * RECORD_SECONDS)):
                frame.append(stream.read(CHUNK))
            data_ar = np.fromstring(''.join(frame),
                                    dtype=np.uint8)
            queue.put(data_ar)
