class Perceptron:
    def __init__(self, pesos, bias):
        self.pesos = pesos
        self.bias = bias

    def feed(self, inputs):
        sum = 0
        assert (len(inputs) == len(self.pesos))
        for i in range(0, len(inputs)):
            sum += inputs[i] * self.pesos[i]
        sum += self.bias
        return sum > 0


class AND(Perceptron):

    def __init__(self):
        super().__init__([1, 1], -1.5)


class OR(Perceptron):

    def __init__(self):
        super().__init__([1, 1], -0.5)


class NAND(Perceptron):
    def __init__(self):
        super().__init__([-2, -2], 3)


class SummingNumbers:

    def __init__(self):
        self.NAND1 = NAND()

    def feed(self, x1, x2):
        uno = self.NAND1.feed([x1, x2])
        dos = self.NAND1.feed([x1, uno])
        tres = self.NAND1.feed([uno, x2])
        sum = self.NAND1.feed([dos, tres])
        carry = self.NAND1.feed([uno, uno])
        return sum, carry


if __name__ == "__main__":
    suma = SummingNumbers()
    print(suma.feed(1, 1))
