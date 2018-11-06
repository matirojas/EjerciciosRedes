class NeuralLayer:
    def __init__(self, neurons, outputs=[]):
        self.neurons = neurons

    def feed(self, someInputValues):
        for i in range(1, len(self.neurons)):
            self.outputs.append(self.neurons[i].feed(self, someInputValues))
        return self.outputs

    def backwardPropagateError(self, expectedOutputs):
        for i in range(0,len(self.neurons)):
            self.neurons[i].backwardPropagateError(self, expectedOutputs)

    def updateWeights(self):