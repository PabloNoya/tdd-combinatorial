from unittest import TestCase
from main.combinatorial import Combinatorial


class CombinatorialTests(TestCase):
    def test_x_mayor_n(self):
        comb = Combinatorial(x=2, n=1)

        self.assertGreater(comb.x, comb.n)
        self.assertEqual(comb.calculate(), 0)
