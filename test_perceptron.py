from unittest import TestCase

from Perceptor import NAND
from Perceptor import OR
from Perceptor import AND


class TestPerceptron(TestCase):
    def test_feed(self):
        AND1 = AND()
        NAND1 = NAND()
        OR1 = OR()
        self.assertEqual(AND1.feed([1, 1]), 1)
        self.assertEqual(AND1.feed([1, 0]), 0)
        self.assertEqual(AND1.feed([0, 1]), 0)
        self.assertEqual(AND1.feed([0, 0]), 0)
        self.assertEqual(NAND1.feed([1, 1]), 0)
        self.assertEqual(NAND1.feed([1, 0]), 1)
        self.assertEqual(NAND1.feed([0, 1]), 1)
        self.assertEqual(NAND1.feed([0, 0]), 1)
        self.assertEqual(OR1.feed([1, 1]), 1)
        self.assertEqual(OR1.feed([1, 0]), 1)
        self.assertEqual(OR1.feed([0, 1]), 1)
        self.assertEqual(OR1.feed([0, 0]), 0)
