#!/usr/bin/env python

from ImageFile import ImageFile
from LabelFile import LabelFile
from neuralnetwork import NeuralNetwork
import numpy as np

from sklearn.metrics import classification_report

def runProgram():
    print("loading training data ")

    # na czas testowania dałem dane do walidacje jako dane na podstawi których sieć się uczy
    trainLabel = LabelFile('./data/train-labels-idx1-ubyte') 
    trainImages = ImageFile('./data/train-images-idx3-ubyte')
    #trainLabel = LabelFile('./data/t10k-labels-idx1-ubyte') 
    #trainImages = ImageFile('./data/t10k-images-idx3-ubyte')

    print("loading end ")
    print("loaded training images {}".format(trainLabel.label_count))

    print("loading testing data ")
    testLabel = LabelFile('./data/t10k-labels-idx1-ubyte') 
    testImages = ImageFile('./data/t10k-images-idx3-ubyte')
    print("loading end ")
    print("loaded testing images {}".format(testLabel.label_count))



    print("array convertion")
    xdI = np.array(trainImages.imagesOneDim)
    xdITestowe = np.array(testImages.imagesOneDim)

    xdL = np.array(trainLabel.testV2)
    xdLTestowe = np.array(testLabel.testV2)
    print("array ended")

    print("creating network ")
#    imageNetwork = NeuralNetwork([784, 392, 196, 48, 24, 10], alpha=0.2)
#    imageNetwork = NeuralNetwork([xdI.shape[1], 392, 196, 10], alpha=0.2)
    imageNetwork = NeuralNetwork([xdI.shape[1], 196, 10], alpha=0.2)
    print("[INFO] {}".format(imageNetwork))

    print("network training started")
    imageNetwork.fit(xdI, xdL, epochs=100)
    print("network training ended")

    predictions = imageNetwork.predict(xdITestowe)
    predictions = predictions.argmax(axis=1)
    print(classification_report(xdLTestowe.argmax(axis=1), predictions))


def test():
    return LabelFile('./data/t10k-labels-idx1-ubyte')

def main():
    1
    print("test")
    test()
    runProgram()

 
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
