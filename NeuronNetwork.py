from Neuron import Neuron
from NeuronLayer import NeuronLayer
from random import random, uniform, randint
import math
import matplotlib.pyplot as plt
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
        listaAciertos = []
        errorEpoca = []
        for i in range(0, epoch):
            error = 0
            aciertos = 0
            for j in range(len(inputSet)):
                aux = self.feed(inputSet[j])
                error += math.pow(expectedOutputs[j][0] - aux[0], 2)

                if aux[0] >= 0.5:
                    aux[0] = 1
                    if aux[0] == expectedOutputs[j][0]:
                        aciertos += 1
                elif aux[0] < 0.5:
                    aux[0] = 0
                    if aux[0] == expectedOutputs[j][0]:
                        aciertos += 1

                self.backwardPropagateError(expectedOutputs[j])
                self.updateWeigths()
            listaAciertos.append(aciertos/len(inputSet))
            errorEpoca.append(error)

        plt.plot(range(0, epoch), listaAciertos)
        plt.xlabel("Number of Epoch")
        plt.ylabel("Fracción de aciertos")
        plt.title("Curva de aprendizaje")
        plt.show()
        plt.plot(range(0, epoch), errorEpoca)
        plt.xlabel("Number of Epoch")
        plt.ylabel("MSE")
        plt.title("Error cuadrático medio")
        plt.show()
