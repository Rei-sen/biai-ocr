
#!/usr/bin/env python

import re

class PGMImage:
    def __init__(self, path):
        with open(path, 'r') as f:
            rawData = f.read()
            data = re.sub(r'#.*\n', r'', rawData).split()
            self.magic = data[0]
            self.width = data[1]
            self.height = data[2]
            self.data = [int(i) for i in data[3:]]
