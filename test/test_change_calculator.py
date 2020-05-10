import unittest
from unittest.mock import MagicMock, call

from change_calculator.change_calculator import ChangeCalculator
from change_calculator.exceptions import (CalculationError,
                                          NegativeChangeAmountError,
                                          NegativeCoinError,
                                          NegativeCountError)


class TestChangeCalculator(unittest.TestCase):

    def setUp(self):
        def return_argument(argument):
            return argument
        self.algorithm = MagicMock()
        self.algorithm.sort_coins.side_effect = return_argument
        self.change_calculator = ChangeCalculator(self.algorithm)

    def test_initialise_empty_coins(self):
        coins = {}
        self.change_calculator.initialise(coins)
        self.algorithm.sort_coins.assert_called_with(coins)

    def test_initialise_with_negative_coin(self):
        with self.assertRaises(NegativeCoinError):
            self.change_calculator.initialise({-1:1})

    def test_initialise_with_negative_count(self):
        with self.assertRaises(NegativeCountError):
            self.change_calculator.initialise({1:-1})

    def test_add_empty_coins(self):
        coins = {}
        self.change_calculator.initialise(coins)
        self.change_calculator.add_coins(coins)

        self.algorithm.sort_coins.has_calls(
            [call(coins), call(coins)]
        )

    def test_add_coins_to_empty(self):
        coins = {1:1}
        self.change_calculator.initialise({})
        self.change_calculator.add_coins(coins)

        self.algorithm.sort_coins.has_calls(
            [call({}), call(coins)]
        )
        self.assertEqual(coins, self.change_calculator._coins)

    def test_add_coins_to_coins(self):
        coins = {1:1}
        self.change_calculator.initialise(coins)
        self.change_calculator.add_coins(coins)

        self.algorithm.sort_coins.has_calls(
            [call(coins), call(coins)]
        )
        self.assertEqual({1:2}, self.change_calculator._coins)

    def test_get_change_with_negative_amount(self):
        with self.assertRaises(NegativeChangeAmountError):
            self.change_calculator.get_change(-1)

    def test_get_change(self):
        coins = {1:5, 2:10}
        self.change_calculator.initialise(coins)
        self.algorithm.calculate_coins.return_value = {1:1, 2:2}

        self.assertEqual({1:1, 2:2}, self.change_calculator.get_change(5))
        self.algorithm.calculate_coins.has_calls(
            [call(1)]
        )
        self.assertEqual({1:4, 2:8}, self.change_calculator._coins)
