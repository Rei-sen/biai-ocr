#!/usr/bin/env python

import struct

class Image:
    def __init__(self):
        self.data = []

class ImageFile:
    def __init__(self, path):
        with open(path, 'rb') as f:
            header = struct.unpack(">iiii", f.read(16))
            self.magic = header[0]
            self.image_count = header[1]
            self.rows_per_image = header[2]
            self.cols_per_image = header[3]
        self.imagse = []

def main():
    1

if __name__ == '__main__':
    main()
