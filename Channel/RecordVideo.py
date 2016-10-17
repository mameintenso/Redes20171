#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import numpy as np
import cv2
from cStringIO import StringIO
from threading import Thread

def toString(data):
    f = StringIO()
    np.lib.format.write_array(f, data)
    return f.getvalue()

class VideoRecorder(Thread):

    def __init__(self, client):
        super(VideoRecorder, self).__init__()
        self.client = client
        self.recording = True

    def run(self):
        self.video = cv2.VideoCapture(0)
        cap = self.video
        self.recording = True
        while self.recording:
            ret, frame = cap.read()
            print 'ret: ' + str(ret)
            cv2.imshow('Grabando video....', frame)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
            data = xmlrpclib.Binary(toString(frame))
            self.client.play_video(data)
        cap.release()
        cv2.destroyAllWindows()

    def stop_video(self):
        print "recording ended by the user"
        self.recording = False
        self.client.stop_video()
        # cap = self.video
        # cv2.destroyAllWindows()
        # cap.release()
