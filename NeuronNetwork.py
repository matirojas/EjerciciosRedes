from Neuron import Neuron
from NeuronLayer import NeuralLayer


class NeuralNetwork:
    def __init__(self, firstLayer, lastLayer, layers):
        self.firstLayer = firstLayer
        self.lastLayer = lastLayer
        self.layers = layers
        self.outputs = []
        self.delta = 0


    def feed(self, inputs):
        result = self.firstLayer.feed(inputs)
        for i in range(1, len(self.layers)):
            result = self.layers[i].feed(result)
        return self.lastLayer.outputs

    def train(self, inputs, desiredOutput):
        outputs = self.feed(inputs)

        return "the error"

    def backwardPropagateError(self,expectedOutputs):


    def updateWeight(self,inputs):

if __name__ == "__main__":
    neuron1 = Neuron([-2, 2], -1.5, 0.1)
    neuron2 = Neuron([-2, 2], -1.5, 0.1)
    firstLayer = NeuralLayer(neuron1)
    lastLayer = NeuralLayer(neuron2)
    neuralNetwork = NeuralNetwork(firstLayer, lastLayer, [firstLayer, lastLayer])
    print(neuralNetwork.feed([[0, 0], [0, 1], [1, 0], [1, 1]]))
