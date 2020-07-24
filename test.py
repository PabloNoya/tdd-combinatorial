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

    def test_x_0_n_3(self):
        comb = Combinatorial(x=0, n=3)
        self.assertEqual(6, comb.calculate())

    def test_x_1_n_4(self):
        comb = Combinatorial(x=1, n=4)
        self.assertEqual(24, comb.calculate())

    def test_x_equal_n(self):
        comb = Combinatorial(x=10, n=10)
        self.assertEqual(1, comb.calculate())

    def test_x_1_n_1(self):
        comb = Combinatorial(x=1, n=1)
        self.assertEqual(comb.x, comb.n)
        self.assertEqual(1, comb.calculate())

