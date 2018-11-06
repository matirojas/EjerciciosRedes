from random import random, uniform, randint
import matplotlib.pyplot as plt
from Perceptor import Perceptron


class LearningCurve:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.randomweights = [uniform(-2, 2), uniform(-2, 2)]
        self.bias = random()
        self.perceptron = Perceptron(self.randomweights, self.bias, 0.1)

    def learningCurve(self):
        razon = []
        largo = len(self.inputs)
        for i in range(0, 1000):
            answers = []
            correctas = 0
            testingset = []
            testingoutputs = []
            # Training the perceptron
            for j in range(0, largo):
                random = randint(0, largo - 1)
                self.perceptron.training(self.inputs[random], self.outputs[random])
            for i in range(0, 100):
                random = randint(0, len(self.inputs)-1)
                testingset.append(self.inputs[random])
                testingoutputs.append(self.outputs[random])
            for i in range(0, len(testingset)):
                answers.append(self.perceptron.feed(testingset[i]))
                if answers[i] == testingoutputs[i]:
                    correctas += 1

            correctas = correctas / len(answers)
            razon.append(correctas)

        plt.plot(range(0, 1000), razon)
        plt.ylim((0, 1))
        plt.ylabel("Porcentaje de aciertos")
        plt.xlabel("# Entrenamientos")
        plt.title("Learning Curve")
        plt.show()


if __name__ == "__main__":
    inputs = [[0, 1], [1, 0], [0, 0], [1, 1]]
    outputs = [1, 1, 1, 0]
    grafics = LearningCurve(inputs, outputs)
    grafics.learningCurve()
