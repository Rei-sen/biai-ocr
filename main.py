#!/usr/bin/env python

import struct

class Image:
    def __init__(self):
        self.data = [[]]

class ImageFile:
    def __init__(self, path):
        with open(path, 'rb') as f:
            header = struct.unpack(">iiii", f.read(16))
            self.magic = header[0]
            self.image_count = header[1]
            self.rows_per_image = header[2]
            self.cols_per_image = header[3]
            self.images = []

            for img in range(self.image_count):
                img = []
                for row in range(self.rows_per_image):
                    row = []
                    for col in range(self.cols_per_image):
                        row.append(f.read(1))
                    img.append(row)
                self.images.append(img)

class LabelFile:
    def __init__(self, path):
        with open(path, 'rb') as f:
            header = struct.unpack(">ii", f.read(8))
            self.magic = header[0]
            self.label_count = header[1]
            self.labels = f.read()

def main():
    1

if __name__ == '__main__':
    main()
