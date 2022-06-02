
#!/usr/bin/env python

import struct

from numpy import imag

class ImageFile:
    def __init__(self, path):
        with open(path, 'rb') as f:
            header = struct.unpack(">iiii", f.read(16))
            self.magic = header[0]
            self.image_count = header[1]
            self.rows_per_image = header[2]
            self.cols_per_image = header[3]
            self.imagesOneDim = []
            i = 0
            for img in range(self.image_count):
                whole = []
                for row in range(self.rows_per_image):
                    for col in range(self.cols_per_image):
                        whole.append(int.from_bytes(f.read(1), "big") / 255.0)
                if i == 0:
                    print("size of picture {}".format(len(whole)))
                i+=1
                self.imagesOneDim.append(whole)
