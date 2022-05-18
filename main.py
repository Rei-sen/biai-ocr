#!/usr/bin/env python

from ImageFile import ImageFile
from LabelFile import LabelFile
from neuralnetwork import NeuralNetwork
from PGMImage import PGMImage
import numpy as np
import sys



def test():
    return LabelFile('./data/t10k-labels-idx1-ubyte')

def usage():
    print(sys.argv[0] + ' train/read')

def train():
    if (len(sys.argv) <= 5):
        print('usage:\n' + sys.argv[0] + 'train image-path label-path output-path')
    else:
        img = ImageFile(sys.argv[2])
        labels = LabelFile(sys.argv[3])

def read():
    if (len(sys.argv) <= 5):
        print('usage:\n' + sys.argv[0] + 'read network-path image-path')
    else:
        img = PGMImage(sys.argv[3])

def main():
    print("test")
    test()

 
    #region xor network usage example
    """
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    xOrTest = NeuralNetwork([2, 2, 1], alpha=0.5)
    xOrTest.fit(X, y, epochs=2000)
    for (x, target) in zip(X, y):
        # make a prediction on the data point and display the result
        # to our console
        pred = xOrTest.predict(x)[0][0]
        step = 1 if pred > 0.5 else 0
        print("[INFO] data={}, ground-truth={}, pred={:.4f}, step={}".format(
            x, target[0], pred, step))
    """
    #endregion

    args = sys.argv
    if (len(args) >= 2):
        if (args[1] == 'train'):
            train()
        elif (args[1] == 'read'):
            read()
    else:
        print("usage:")
        usage()



if __name__ == '__main__':
    main()
