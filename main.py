#!/usr/bin/env python

from ImageFile import ImageFile
from LabelFile import LabelFile
from neuralnetwork import NeuralNetwork
import numpy as np



def test():
    return LabelFile('./data/t10k-labels-idx1-ubyte')

def main():
    1
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




if __name__ == '__main__':
    main()
