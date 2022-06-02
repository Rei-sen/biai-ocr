
#!/usr/bin/env python

import re

class PGMImage:
    def __init__(self, path):
        with open(path, 'r') as f:
            rawData = f.read()
            data = re.sub(r'#.*\n', r'', rawData).split()
            self.magic = data[0]
            self.width = int(data[1])
            self.height = int(data[2])
            self.maxValue = int(data[3])
            self.data = [int(i)/self.maxValue for i in data[4:]]
