# Class that represent an artificial neuron

class Perceptron:

    # We have the constructor of a Perceptron that takes 3 arguments.
    # The first argument is the weight, second the bias and the third
    # argument is the learningRate.

    def __init__(self, weight, bias, learningRate):
        self.weight = weight  # Weight is a list
        self.bias = bias
        self.learningRate = learningRate

    def feed(self, inputs):  # We can feed the Perceptron with some inputs
        assert len(inputs) == len(self.weight)  # The number of inputs has to be the same that weight
        equation = 0
        for i in range(0, len(inputs)):
            equation = equation + (inputs[i] * self.weight[i])
        equation = equation + self.bias  # We calcule the value of the equation
        if equation > 0:
            return 1  # If equation > 0 the output is 1
        else:
            return 0  # otherwise the output is 0

    def training(self, inputs, desiredOutputs):  # We can train the Perceptron now with some inputs and desired outputs
        realOutput = self.feed(inputs)
        diff = desiredOutputs - realOutput
        for i in range(0, len(inputs)):
            self.weight[i] = self.weight[i] + (self.learningRate * inputs[i] * diff)
        self.bias = self.bias + (self.learningRate * diff)
