import unittest
from unittest.mock import MagicMock, call

from change_calculator.change import Change


class TestChange(unittest.TestCase):

    def test_initialisation_without_coins(self):
        change = Change({})

        self.assertEqual({}, change.coins)
        self.assertEqual(0, change.number_of_coins)

    def test_initialisation_with_single_coin(self):
        coins = {1:1}
        change = Change(coins)

        self.assertEqual(coins, change.coins)
        self.assertEqual(1, change.number_of_coins)

    def test_initialisation_with_multiple_coins(self):
        coins = {1:1, 2:2, 3:3, 4:10}
        change = Change(coins)

        self.assertEqual(coins, change.coins)
        self.assertEqual(16, change.number_of_coins)

    def test_adding_single_coins(self):
        coins = {1:1}
        change = Change(coins) + Change(coins)

        self.assertEqual({1:2}, change.coins)
        self.assertEqual(2, change.number_of_coins)

    def test_adding_multiple_coins(self):
        coins = {1:1, 2:2, 3:3, 4:10}
        change = Change(coins) + Change(coins)

        self.assertEqual({1:2, 2:4, 3:6, 4:20}, change.coins)
        self.assertEqual(32, change.number_of_coins)

    def test_positive_equality(self):
        coins = {1:1, 2:2, 3:3, 4:10}

        self.assertEqual(Change(coins), Change(coins))

    def test_negative_equality(self):
        self.assertNotEqual(Change({}), Change({1:1, 2:2, 3:3, 4:10}))

    def test_lt(self):
        self.assertLess(Change({}), Change({1:1, 2:2, 3:3, 4:10}))

    def test_not_lt(self):
        self.assertFalse(Change({1:1, 2:2, 3:3, 4:10}) < Change({}))

    def test_gt(self):
        self.assertGreater(Change({1:1, 2:2, 3:3, 4:10}), Change({}))

    def test_not_gt(self):
        self.assertFalse(Change({}) > Change({1:1, 2:2, 3:3, 4:10}))

    def test_total(self):
        change = Change({1:1, 2:2, 3:3, 4:10})

        self.assertEqual(54, change.total())

    def test_zero_total(self):
        change = Change({})

        self.assertEqual(0, change.total())
