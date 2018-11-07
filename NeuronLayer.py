class NeuralLayer:
    def __init__(self, neurons, outputs=[], nextLayer=None, PreviousLayer = None):
        self.outputs = outputs
        self.neurons = neurons
        self.nextLayer = nextLayer
        self.PreviousLayer = PreviousLayer

    def feed(self, someInputValues):
        for i in range(1, len(self.neurons)):
            self.outputs.append(self.neurons[i].feed(someInputValues))
        return self.outputs

    def getNeurons(self):
        return self.neurons

    def backwardPropagateLastLayer(self, expectedOutput):
        for neuron in self.neurons:
            neuron.backwardPropagateError(expectedOutput)

    def backwardPropagateHiddenLayer(self):
        for i in range(0, len(self.neurons)):
            newValue = self.neurons[i + 1].getWeight() * self.neurons[i + 1].getDelta()
            self.neurons[i].setNewDelta(newValue)

    def updateWeights(self):
        for i in range(0, len(self.neurons)):
            value = self.PreviousLayer.outputs
            self.neurons[i].setWeight(value)