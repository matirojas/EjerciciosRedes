from Neuron import Neuron
from NeuronLayer import NeuronLayer
from random import random, uniform, randint
import math

import numpy as np


class NeuronNetwork:
    def __init__(self, layers=[]):
        self.layers = layers
        self.output = 0
        for i in range(len(self.layers)):
            if i == 0:
                self.layers[i].updateLayers(self.layers[i + 1], None)
            if i == len(self.layers) - 1:
                self.layers[i].updateLayers(None, self.layers[i - 1])
            else:
                self.layers[i].updateLayers(self.layers[i + 1], self.layers[i - 1])

    def feed(self, inputs):
        result = self.layers[0].feed(inputs)
        for i in range(1, len(self.layers)):
            result = self.layers[i].feed(result)
        self.output = result
        return self.output

    def backwardPropagateError(self, expectedOutputs):
        self.layers[-1].backwardPropagateLastLayer(expectedOutputs)
        for i in reversed(range(len(self.layers) - 1)):
            self.layers[i].backwardPropagateHiddenLayer()

    def updateWeigths(self):
        for i in range(len(self.layers)):
            self.layers[i].updateWeights()

    def training(self, inputSet, expectedOutputs, epoch):
        for i in range(0, epoch):
            for j in range(len(inputSet)):

                self.feed(inputSet[j])

                self.backwardPropagateError(expectedOutputs[j])
                self.updateWeigths()


if __name__ == '__main__':


    Neuron1 = Neuron([0.7, 0.3], 0.5, 0.5)
    Neuron2 = Neuron([0.3, 0.7], 0.4, 0.5)
    Neuron3 = Neuron([0.2, 0.3], 0.3, 0.5)
    Neuron4 = Neuron([0.4, 0.2], 0.6, 0.5)
    Layer1 = NeuronLayer([Neuron1, Neuron2])
    Layer2 = NeuronLayer([Neuron3, Neuron4])
    Red2 = NeuronNetwork([Layer1, Layer2])
    Red2.training([[1, 1]], [[1, 1]], 1)
    print(Neuron1.getWeight())
    print(Neuron1.getBias())
    print(Neuron2.getWeight())
    print(Neuron2.getBias())
    print(Neuron3.getWeight())
    print(Neuron3.getBias())
    print(Neuron4.getWeight())
    print(Neuron4.getBias())
