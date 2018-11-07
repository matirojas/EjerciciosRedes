from Neuron import Neuron
from NeuronLayer import NeuralLayer


class NeuralNetwork:
    def __init__(self, firstLayer, lastLayer, layers):
        self.firstLayer = firstLayer
        self.lastLayer = lastLayer
        self.layers = layers
        self.output = []

    def feed(self, inputs): # Se le entregan los inputs a la red neuronal y obtiene el conjunto de outputs
        result = self.firstLayer.feed(inputs)
        for i in range(1, len(self.layers)):
            result = self.layers[i].feed(result)
        self.output = self.lastLayer.outputs
        return self.output

    def backwardPropagateError(self, expectedOutputs):
        self.lastLayer.backwardPropagateLastLayer(expectedOutputs)
        for layer in reversed(range(len(self.layers - 1))):
            layer.backwardPropagateHiddenLayer(expectedOutputs)

    def updateWeigths(self):
        for i in range(0, len(self.layers)):
            self.layers[i].updateWeights()


