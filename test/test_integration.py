import unittest
from unittest.mock import MagicMock, call

from change_calculator.calculators import Calculators
from change_calculator.change_algorithm import (DynamicProgrammingAlgorithm,
                                                GreedyAlgorithm)
from change_calculator.exceptions import CalculationError


class TestCanonicalIntegration(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculators.canonical()

    def test_creation(self):
        self.assertEqual(GreedyAlgorithm, type(self.calculator._change_algorithm))

    def test_get_change(self):
        self.calculator.initialise({1:1, 2:1, 5:1, 10:1})
        self.assertEqual({1:1, 2:1, 5:1, 10:1}, self.calculator.get_change(18))

    def test_get_change_removes_coins(self):
        self.calculator.initialise({1:1, 2:1, 5:1, 10:1})
        self.calculator.get_change(18)
        with self.assertRaises(CalculationError):
            self.calculator.get_change(1)

    def test_get_added_coins(self):
        self.calculator.initialise({1:1, 2:1, 5:1, 10:1})
        self.calculator.add_coins({1:1, 50:1})
        self.assertEqual({1:2, 2:1, 5:1, 10:1, 50:1}, self.calculator.get_change(69))
