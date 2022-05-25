#!/usr/bin/env python

from asyncio.windows_events import NULL
from ImageFile import ImageFile
from LabelFile import LabelFile
from neuralnetwork import NeuralNetwork
import numpy as np
import pickle

from sklearn.metrics import classification_report

def displayWrong(indexArray, images, labels, prediction):
    maxDisplays = 50
    for index in indexArray:
        numberImage = images.imagesOneDim[index]
        print("Displaying inncorect prediction!!\n Predicted {} while the value is {}".format(prediction[index], labels[index]))
        i = 0
        for x in range(1,29):
            toDisplay = ""
            for y in range(1,29):
                toDisplay += str(numberImage[i])
                i+=1
            print(toDisplay)
        print("\n\n\n")
        maxDisplays-=1
        if maxDisplays<=0:
            break


def displayWrongPredictions(prediction, labels, images):
    i = 0
    wrongIndexArray = []
    for pred in prediction:
        if pred != labels[i]:
            wrongIndexArray.append(i)
        i+=1
    displayWrong(wrongIndexArray, images, labels, prediction)


def saveClass(networkClass, name):
    with open(f'' + "{}".format(name), 'wb') as file:
        pickle.dump(networkClass, file)

def loadeClass(name):
    with open(f''+ "{}".format(name), 'rb') as file2:
        s1_new = pickle.load(file2)
    if s1_new == NULL:
        print("Network load failed")
        return NULL
    return s1_new

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


# commentef for file saving testing
#    imageNetwork = NeuralNetwork([xdI.shape[1], 10], alpha=0.1)
#    print("[INFO] {}".format(imageNetwork))

#    print("network training started")
#    imageNetwork.fit(xdI, xdL, epochs=1)
#    print("network training ended")
 
    imageNetwork = loadeClass('test.pickle')
#    saveClass(imageNetwork, 'test.pickle')


    predictions = imageNetwork.predict(xdITestowe)
    predictions = predictions.argmax(axis=1)
    displayWrongPredictions(predictions, testLabel.test, testImages)
    print(classification_report(xdLTestowe.argmax(axis=1), predictions))


def test():
    return LabelFile('./data/t10k-labels-idx1-ubyte')

def main():
    1
    print("test")
    test()
    runProgram()

    fileName = 'test.pickle'

 
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
