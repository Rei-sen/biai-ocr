#!/usr/bin/env python

import struct


class LabelFile:
    def __init__(self, path):
        self.labelValue = list()
        with open(path, 'rb') as f:
            header = struct.unpack(">ii", f.read(8))
            self.magic = header[0]
            self.label_count = header[1]
            self.labels = f.read()
        self.labelValue = list(self.labels)
        self.labelValueArray=list()

        for x in self.labelValue:
            match x:
                case 0:
                    self.labelValueArray.append([1,0,0,0,0,0,0,0,0,0])
                case 1:
                    self.labelValueArray.append([0,1,0,0,0,0,0,0,0,0])
                case 2:
                    self.labelValueArray.append([0,0,1,0,0,0,0,0,0,0])
                case 3:
                    self.labelValueArray.append([0,0,0,1,0,0,0,0,0,0])
                case 4:
                    self.labelValueArray.append([0,0,0,0,1,0,0,0,0,0])
                case 5:
                    self.labelValueArray.append([0,0,0,0,0,1,0,0,0,0])
                case 6:
                    self.labelValueArray.append([0,0,0,0,0,0,1,0,0,0])
                case 7:
                    self.labelValueArray.append([0,0,0,0,0,0,0,1,0,0])
                case 8:
                    self.labelValueArray.append([0,0,0,0,0,0,0,0,1,0])
                case 9:
                    self.labelValueArray.append([0,0,0,0,0,0,0,0,0,1])

