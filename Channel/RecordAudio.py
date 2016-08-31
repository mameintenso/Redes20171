#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyaudio

from threading import Thread, Event

from Constants.Constants import *

class AudioSender(Thread):
    '''
    Class that sends audio if enqueued in a given
    queue (buffer)
    '''

    def __init__(self, queue, client):
        super(AudioSender, self).__init__()
        self.queue = queue
        self._stop = Event()
        self.client = client

    def run(self):
        while True:
            if not self.queue.empty():
                self.client.send_audio(queue.get())

    def stop(self):
        self._stop.set()

    def is_stop(self):
        return self._stop.isSet()


class AudioRecorder(Thread):
    def __init__(self, queue):
        super(AudioRecorder, self).__init__()

        self.p = pyaudio.PyAudio()
        self.queue = queue
        self.record = True
        self._stop = Event()

    def stop(self):
        self._stop.set()

    def is_stop(self):
        return self._stop.isSet()

    def run(self):
        '''
        Records audio and saves it in the given
        queue (buffer)
        '''
        stream = self.p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print('recording audio....')
        while self.record:
            data = stream.read(CHUNK)
            self.queue.put(data)
        print("done recording")
        self.record = True
        stream.stop_stream()
        stream.close()
        self.p.terminate()
