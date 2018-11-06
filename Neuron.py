from Perceptron import Perceptron
from cmath import exp
import numpy as np


class Neuron(Perceptron):

    def __init__(self, weights, bias,learningRate):
        super().__init__(weights, bias ,learningRate)
        self.delta = 0
        self.output = 0

    def feed(self, inputs):
        assert len(self.weights) == len(inputs)
        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.weights[i]
        equation = equation + self.bias
        sigma = 1 / (1 + exp(-equation))
        if np.real(sigma) > 0.5:
            self.output = 1
            return self.output
        self.output = 0
        return 1

    def backwardPropagateError(self, expectedOutputs):
        error = expectedOutputs - self.output
        self.delta = error * (1 - self.output)

