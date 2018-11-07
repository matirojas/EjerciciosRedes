from Perceptron import *
from cmath import exp
import numpy as np

class Sigmoid(Perceptron):
    def __init__(self, weights, bias, learningRate):
        super().__init__(weights, bias, learningRate)

    def feed(self, inputs):
        assert len(self.weights) == len(inputs)
        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.weights[i]
        equation = equation + self.bias
        sigma = 1 / (1 + exp(-equation))
        if np.real(sigma) > 0.5:
            return 1
        return 0
