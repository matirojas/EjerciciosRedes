from unittest import TestCase

from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork

# TEST CASES 1 Y 2 ENTREGADOS POR EL PROFESOR

class TestNeuronNetwork(TestCase):
    def test_training(self):
        Neuron1 = Neuron([0.4, 0.3], 0.5, 0.5)
        Neuron2 = Neuron([0.3], 0.4, 0.5)
        Layer1 = NeuronLayer([Neuron1])
        Layer2 = NeuronLayer([Neuron2])
        Red1 = NeuronNetwork([Layer1, Layer2])
        Red1.training([[1, 1]], [[1]], 1)
        assert Neuron1.getBias() == 0.502101508999489
        assert Neuron1.getWeight() == [0.40210150899948904, 0.302101508999489]
        assert Neuron2.getBias() == 0.43937745312797394
        assert Neuron2.getWeight() == [0.33026254863991883]

        Neuron5 = Neuron([0.7, 0.3], 0.5, 0.5)
        Neuron6 = Neuron([0.3, 0.7], 0.4, 0.5)
        Neuron7 = Neuron([0.2, 0.3], 0.3, 0.5)
        Neuron8 = Neuron([0.4, 0.2], 0.6, 0.5)
        Layer3 = NeuronLayer([Neuron5, Neuron6])
        Layer4 = NeuronLayer([Neuron7, Neuron8])
        Red2 = NeuronNetwork([Layer3, Layer4])
        Red2.training([[1, 1]], [[1, 1]], 1)
        assert Neuron5.getWeight() == [0.7025104485493278, 0.3025104485493278]
        assert Neuron5.getBias() == 0.5025104485493278
        assert Neuron6.getWeight() == [0.30249801135748333, 0.7024980113574834]
        assert Neuron6.getBias() == 0.40249801135748337
        assert Neuron7.getWeight() == [0.22994737881955657, 0.32938362863950127]
        assert Neuron7.getBias() == 0.3366295422515899
        assert Neuron8.getWeight() == [0.41943005652646226, 0.21906429169838573]
        assert Neuron8.getBias() == 0.6237654881509048