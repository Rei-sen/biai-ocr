#!/usr/bin/env python

import struct

class LabelFile:
    def __init__(self, path):
        with open(path, 'rb') as f:
            header = struct.unpack(">ii", f.read(8))
            self.magic = header[0]
            self.label_count = header[1]
            self.labels = f.read()
