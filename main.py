#!/usr/bin/env python

from ImageFile import ImageFile
from LabelFile import LabelFile
from neuralnetwork import NeuralNetwork
from PGMImage import PGMImage
import numpy as np
import pickle
import sys

from sklearn.metrics import classification_report

def displayWrong(indexArray, images, labels, prediction):
    for index in indexArray:
        numberImage = images.imagesOneDim[index]
        print("Displaying inncorect prediction!!\nPredicted {} while the value is {}".format(prediction[index], labels[index]))
        i = 0
        for x in range(1,29):
            toDisplay = ""
            for y in range(1,29):
                toDisplay += str(numberImage[i])
                i+=1
            print(toDisplay)
        print("\n\n\n")


def displayWrongPredictions(prediction, labels, images, labelsCount):
    i = 0
    xd = 0
    wrongIndexArray = []
    for pred in prediction:
        if pred != labels[i]:
            wrongIndexArray.append(i)
            xd+=1
        i+=1
    displayWrong(wrongIndexArray, images, labels, prediction)
    print("Good count  bad count {}".format(xd))


def saveClass(networkClass, name):
    with open(f'' + "{}".format(name), 'wb') as file:
        pickle.dump(networkClass, file)

def loadClass(name):
    with open(f''+ "{}".format(name), 'rb') as file2:
        s1_new = pickle.load(file2)
    # if s1_new == NULL:
    #     print("Network load failed")
    #     return NULL
    return s1_new


def trainAndSaveNetwork(imagesFile, labelsFile):
    print("loading training data ")
    trainLabel = LabelFile('./data/train-labels-idx1-ubyte') 
    trainImages = ImageFile('./data/train-images-idx3-ubyte')
    print("loading end ")
    print("array convertion")
    convertImages = np.array(trainImages.imagesOneDim)
    convertLabels = np.array(trainLabel.labelValueArray)
    print("array ended")    

    print("creating network ")
    imageNetwork = NeuralNetwork([convertImages.shape[1], 392, 196, 49, 10], alpha=0.05)
    print("network training started")
    imageNetwork.fit(convertImages, convertLabels, epochs=200)
    print("network training ended")
    saveClass(imageNetwork, 'test.pickle')


def testNetwork(imagesFile, labelsFile, networkFile, displayWrong):
    print("loading testing data ")
    testLabel = LabelFile('./data/t10k-labels-idx1-ubyte') 
    testImages = ImageFile('./data/t10k-images-idx3-ubyte')
    print("loading end ")
    print("loaded testing images {}".format(testLabel.label_count))    

    print("array convertion")
    testoweImagesConvert = np.array(testImages.imagesOneDim)
    testoweLabelsgesConvert = np.array(testLabel.labelValueArray)
    print("array ended")
    imageNetwork = loadClass('test.pickle')
    predictions = imageNetwork.predict(testoweImagesConvert)
    predictions = predictions.argmax(axis=1)
    
    if displayWrong == True:
        displayWrongPredictions(predictions, testLabel.labelValue, testImages, testLabel.labelValue.count)
    
    print(classification_report(testoweLabelsgesConvert.argmax(axis=1), predictions))


def runProgram():
    print("loading training data ")

    # na czas testowania dałem dane do walidacje jako dane na podstawi których sieć się uczy
    trainLabel = LabelFile('./data/train-labels-idx1-ubyte') 
    trainImages = ImageFile('./data/train-images-idx3-ubyte')
    
    # prawidłowe dane do walidacji
#    trainLabel = LabelFile('./data/t10k-labels-idx1-ubyte') 
#    trainImages = ImageFile('./data/t10k-images-idx3-ubyte')

    print("loading end ")
    print("loaded training images {}".format(trainLabel.label_count))

    print("loading testing data ")
    testLabel = LabelFile('./data/t10k-labels-idx1-ubyte') 
    testImages = ImageFile('./data/t10k-images-idx3-ubyte')
    print("loading end ")
    print("loaded testing images {}".format(testLabel.label_count))



    print("array convertion")
    xdI = np.array(trainImages.imagesOneDim)
    # get only XX of images
 #   xdI = xdII[:len(xdII)//2]
    xdITestowe = np.array(testImages.imagesOneDim)


    xdL = np.array(trainLabel.labelValueArray)
     # get only XX of images
#    xdL = xdLL[:len(xdLL)//2]
    xdLTestowe = np.array(testLabel.labelValueArray)


    print("array ended")

    print("creating network ")
#    imageNetwork = NeuralNetwork([784, 392, 196, 48, 24, 10], alpha=0.2)
    imageNetwork = NeuralNetwork([xdI.shape[1], 392, 196, 49, 10], alpha=0.05)


# commentef for file saving testing
#    imageNetwork = NeuralNetwork([xdI.shape[1],392,100, 50, 10], alpha=0.05)
#    print("[INFO] {}".format(imageNetwork))

    print("network training started")
    imageNetwork.fit(xdI, xdL, epochs=200)
    print("network training ended")
 
#    imageNetwork = loadClass('test.pickle')
    saveClass(imageNetwork, 'test.pickle')


    predictions = imageNetwork.predict(xdITestowe)
    predictions = predictions.argmax(axis=1)
    
#    displayWrongPredictions(predictions, testLabel.test, testImages, testLabel.test.count)
    print(classification_report(xdLTestowe.argmax(axis=1), predictions))

def usage():
    print(sys.argv[0] + ' train/read/test')

def train():
    if (len(sys.argv) < 6):
        print('usage:\n' + sys.argv[0] + ' train image-path label-path epochs-count output-path')
        return
    img = ImageFile(sys.argv[2])
    labels = LabelFile(sys.argv[3])
    epochsCount = int(sys.argv[4]) # sprawdzenie błędów trzeba dodać
    outputFile = sys.argv[5]

    imgArray = np.array(img.imagesOneDim)
    labelArray = np.array(labels.labelValueArray)

    imageNetwork = NeuralNetwork([imgArray.shape[1], 392, 196, 49, 10], alpha=0.05)
    imageNetwork.fit(imgArray, labelArray, epochs=epochsCount)
    saveClass(imageNetwork, outputFile)


def read():
    if (len(sys.argv) < 4):
        print('usage:\n' + sys.argv[0] + ' read network-path image-path')
        return
    networkPath = sys.argv[2]
    img = PGMImage(sys.argv[3])

    network = loadClass(networkPath)
    print(network.predict([img.data]).argmax(axis=1)[0])

def test():
    if (len(sys.argv) < 4):
        print('usage:\n' + sys.argv[0] + ' test network-path image-path label-path')
        return

    networkPath = sys.argv[2]
    img = ImageFile(sys.argv[3])
    labels = LabelFile(sys.argv[4])

    network = loadClass(networkPath)
    predictions = network.predict(img.imagesOneDim)
    predictions = predictions.argmax(axis=1)

    print(classification_report(labels.labelValue , predictions))

def main():

#    fileName = 'test.pickle'
 #   runProgram()
    #testNetwork("","","",True)

    args = sys.argv
    if (len(args) >= 2):
        if (args[1] == 'train'):
            train()
        elif (args[1] == 'read'):
            read()
        elif (args[1] == 'test'):
            test()
    else:
        print("usage:")
        usage()



if __name__ == '__main__':
    main()
