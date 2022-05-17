#!/usr/bin/env python

import struct


class LabelFile:
    def __init__(self, path):
        self.test = list()
        with open(path, 'rb') as f:
            header = struct.unpack(">ii", f.read(8))
            self.magic = header[0]
            self.label_count = header[1]
            self.labels = f.read()
        self.test = list(self.labels)
        self.testV2=list()

        for x in self.test:
            match x:
                case 0:
                    self.testV2.append([1,0,0,0,0,0,0,0,0,0])
                case 1:
                    self.testV2.append([0,1,0,0,0,0,0,0,0,0])
                case 2:
                    self.testV2.append([0,0,1,0,0,0,0,0,0,0])
                case 3:
                    self.testV2.append([0,0,0,1,0,0,0,0,0,0])
                case 4:
                    self.testV2.append([0,0,0,0,1,0,0,0,0,0])
                case 5:
                    self.testV2.append([0,0,0,0,0,1,0,0,0,0])
                case 6:
                    self.testV2.append([0,0,0,0,0,0,1,0,0,0])
                case 7:
                    self.testV2.append([0,0,0,0,0,0,0,1,0,0])
                case 8:
                    self.testV2.append([0,0,0,0,0,0,0,0,1,0])
                case 9:
                    self.testV2.append([0,0,0,0,0,0,0,0,0,1])

