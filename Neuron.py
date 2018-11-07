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
        if np.real(sigma) > 0.5:
            self.output = 1
            return self.output
        self.output = 0
        return self.output

    def setWeight(self, value):
        self.weight += self.weight + (self.learningRate * self.delta * value)
        self.bias += self.bias + (self.learningRate * self.delta)

    def getWeight(self):  # Funciones auxiliares para obtener el peso y
        return self.weight

    def getDelta(self):  # el delta
        return self.delta

    def setNewDelta(self, value):  # Función para settear deltas desde la clase Neural Network
        error = value
        self.delta = error * self.output * (1 - self.output)

    def backwardPropagateError(self,
                               expectedOutputs):  # Este método es el backwardPropagate asociado a la ultima  neurona
        error = expectedOutputs - self.output
        self.delta = error * self.output * (1 - self.output)

    def updateWeight(self, input):
        self.weight = self.weight + (self.learningRate * self.delta * input)
        self.bias = self.bias + (self.learningRate * self.delta)
