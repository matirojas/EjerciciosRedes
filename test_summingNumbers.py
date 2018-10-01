from unittest import TestCase

from Perceptor import SummingNumbers


class TestSummingNumbers(TestCase):
    def test_suma(self):
        Sum = SummingNumbers()
        self.assertEqual(Sum.feed(0, 0), (False, False))
        self.assertEqual(Sum.feed(0, 1), (True, False))
        self.assertEqual(Sum.feed(1, 0), (True, False))
        self.assertEqual(Sum.feed(1, 1), (False, True))
