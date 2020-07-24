from unittest import TestCase
from main.combinatorial import Combinatorial


class CombinatorialTests(TestCase):
    def test_x_mayor_n(self):
        comb = Combinatorial(x=2, n=1)

        self.assertGreater(comb.x, comb.n)
        self.assertEqual(comb.calculate(), 0)

    def test_x_negativo(self):
        comb = Combinatorial(x=-1, n=0)

        self.assertLess(comb.x, 0)
        self.assertEqual(comb.calculate(), 0)

    def test_n_negativo(self):
        comb = Combinatorial(x=2, n=-1)

        self.assertLess(comb.n, 0)
        self.assertEqual(comb.calculate(), 0)