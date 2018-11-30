from Perceptron import Perceptron
from cmath import exp
import numpy as np

class Neuron(Perceptron):  # Creamos una neurona que corresponde a un Sigmoide
    def __init__(self, weights, bias, learningRate):  # Inicializamos los parámetros
        super().__init__(weights, bias, learningRate)
        self.delta = 0  # Setteamos valores iniciales tanto para delta como para el output
        self.output = 0

    def feed(self, inputs):  # Alimentamos a la neurona con la estructura tradicional de un Sigmoide
        assert len(self.weight) == len(inputs)
        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.weight[i]
        equation = equation + self.bias
        sigma = 1 / (1 + exp(-equation))
        self.output = np.real(sigma)
        return self.output

    def getWeight(self):
        return self.weight

    def getDelta(self):
        return self.delta

    def setNewDelta(self, value):
        error = value
        self.delta = error * self.output * (1 - self.output)

    def backwardPropagateError(self,
                               expectedOutputs):
        error = expectedOutputs - self.output
        self.delta = error * self.output * (1 - self.output)

    def getBias(self):
        return self.bias

    def updateWeight(self, input):
        for i in range(len(self.weight)):
            self.weight[i] = self.weight[i] + (self.learningRate * self.delta * input[i])
        self.bias = self.bias + (self.learningRate * self.delta)
