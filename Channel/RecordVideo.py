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

    def __init__(self, queue, client):
        super(VideoRecorder, self).__init__()
        self.queue = queue
        self.client = client

    def run(self):
        self.video = cv2.VideoCapture(0)
        while True:
            ret, frame = self.video.read()
            print 'ret: ' + str(ret)
            # cv2.imshow('Grabando video....', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            data = xmlrpclib.Binary(toString(frame))
            # self.queue.put(data)
            self.client.play_video(data)
        cap.release()
        cv2.destroyAllWindows()
