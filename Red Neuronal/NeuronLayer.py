class NeuronLayer:
    def __init__(self, neurons, outputs=[]):
        self.neurons = neurons
        self.outputs = outputs
        self.nextLayer = None
        self.PreviousLayer = None
        self.inputs = []

    def feed(self, someInputValues):
        self.inputs = someInputValues
        self.outputs = []
        for neuron in self.neurons:
            self.outputs.append(neuron.feed(someInputValues))
        return self.outputs

    def getNeurons(self):
        return self.neurons

    def backwardPropagateLastLayer(self, expectedOutput):
        for i in range(len(self.neurons)):
            self.neurons[i].backwardPropagateError(expectedOutput[i])

    def backwardPropagateHiddenLayer(self):
        for i in range(len(self.neurons)):
            error_i = 0
            for neuron in self.nextLayer.getNeurons():
                    error_i += neuron.getWeight()[i] * neuron.getDelta()

            self.neurons[i].setNewDelta(error_i)

    def updateWeights(self):
        for i in range(len(self.neurons)):
            self.neurons[i].updateWeight(self.getInputs())

    def getInputs(self):
        return self.inputs

    def updateLayers(self, nextLayer, PreviousLayer):
        self.nextLayer = nextLayer
        self.PreviousLayer = PreviousLayer
