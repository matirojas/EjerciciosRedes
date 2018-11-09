import csv
from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
from LearningCurve import LearningCurve
from random import random, uniform, randint


def learning():
    inputs = []
    expectedOutputs = []
    i = 0
    with open('a.csv', newline='', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for row in reader:
            expectedOutputs.append([int(row[3])])
            inputs.append(row[0:3])

    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            inputs[i][j] = int(inputs[i][j])
    for i in range(len(expectedOutputs)):
        for j in range(len(expectedOutputs[j])):
            expectedOutputs[i][j] = int(expectedOutputs[i][j])

    max = 0
    min = 0
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            if int(inputs[i][j]) > max:
                max = inputs[i][j]
            elif inputs[i][j] < min:
                min = inputs[i][j]

    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            inputs[i][j] = (inputs[i][j] - min) * (1 - 0) / (max - min) + 0

    for i in range(len(expectedOutputs)):
        for j in range(len(expectedOutputs[i])):
            expectedOutputs[i][j] = (expectedOutputs[i][j] - 1) * (1 - 0)/ (2 - 1) + 0
    Neuron1 = Neuron([uniform(-2, 2), uniform(-2, 2), uniform(-2, 2)], random(), 0.1)
    Neuron2 = Neuron([uniform(-2, 2), uniform(-2, 2), uniform(-2, 2)], random(), 0.1)
    Neuron3 = Neuron([uniform(-2, 2), uniform(-2, 2), uniform(-2, 2)], random(), 0.1)
    Neuron4 = Neuron([uniform(-2, 2), uniform(-2, 2), uniform(-2, 2)], random(), 0.1)
    Layer1 = NeuronLayer([Neuron1, Neuron2, Neuron3])
    Layer2 = NeuronLayer([Neuron4])
    Red = NeuronNetwork([Layer1, Layer2])
    Red.training(inputs, expectedOutputs, 100)




learning()
