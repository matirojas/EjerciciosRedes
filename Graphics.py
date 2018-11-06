from Perceptor import Perceptron # We are going to train a see results from Perceptrons
from random import random, uniform
import matplotlib.pyplot as plt


# First we are going to define some auxiliary functions to use on the training


# Function that represent a linear straight

def function(input):
    output = 3 * input + 1
    return output


# This function tells if the point
def whereIs(input):
    expected = function(input[0])  # First we get the expected value
    result = 0
    if input[1] > expected:  # If the value returned from the trained neuron is high than expected, then we return 1
        result = 1
    return result


# With this class we are going to see the result of training the Perceptron
class Graphics:
    def __init__(self):
        self.bias = random()
        self.randomweights = [uniform(-2, 2), uniform(-2, 2)]
        self.perceptron = Perceptron(self.randomweights, self.bias, 0.1)
        self.randomInputsX = []
        self.randomInputsY = []
        self.perceptronAnswers = []
        self.whereIs = []

        # Now we train the Perceptron with values aleatories

        for i in range(0, 1000):
            X = uniform(0, 100)
            Y = uniform(0, 100)
            self.perceptron.training([X, Y], whereIs([X, Y]))

    def plot(self):
        # We now generate a random set
        for i in range(0, 100):
            self.randomInputsX.append(uniform(0, 100))
            self.randomInputsY.append(uniform(0, 500))
            self.perceptronAnswers.append(self.perceptron.feed([self.randomInputsX[i], self.randomInputsY[i]]))
        plt.scatter(self.randomInputsX, self.randomInputsY, c=self.perceptronAnswers)
        x = range(0, 101)
        y = []
        for i in range(0, 101):
            y.append(function(x[i]))
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    grafics = Graphics()
    grafics.plot()
