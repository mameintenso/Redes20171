#! /usr/bin/env python

import pyaudio

# Constants for audio management
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
