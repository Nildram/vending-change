import unittest

from change_calculator.change_algorithm import ChangeAlgorithm
from change_calculator.exceptions import CalculationError


class TestAlgorithms(unittest.TestCase):

    def test_calculate_coins_greedy(self):
        algorithm = ChangeAlgorithm.create(canonical_coin_system=True)
        self._run_canonical_coins(algorithm)

    def test_calculate_coins_dynamic_programming(self):
        algorithm = ChangeAlgorithm.create(canonical_coin_system=False)
        self._run_canonical_coins(algorithm)
        self._run_non_canonical_coins(algorithm)

    def _run_non_canonical_coins(self, algorithm: ChangeAlgorithm):
        self.assertRaises(CalculationError, algorithm.calculate_coins, {1:1, 3:10}, 5)

        test_cases = [
            # expected, coins, amount
            ({3:2}, {1:10, 3:2}, 6),
            ({1:3, 3:1}, {1:10, 3:1}, 6),
            ({3:2}, {1:10, 3:2, 4:2}, 6),
            ({1:2, 4:1}, {1:10, 3:1, 4:2}, 6),
            ({1:1, 3:1, 5:1}, {1:1, 3:1, 5:1}, 9),
            ({3:1, 65:2, 129:1}, {1:10, 3:10, 5:10, 9:10, 17:10, 33:10, 65:10, 129:10}, 262),
            ({1: 1, 3: 1, 5: 1, 9: 1, 17: 1, 33: 1, 65: 1, 129: 1}, {1:1, 3:1, 5:1, 9:1, 17:1, 33:1, 65:1, 129:1}, 262)
        ]
        for test_case in test_cases:
            with self.subTest(f"coins: {test_case[1]}, amount: {test_case[2]}"):
                self.assertEqual(test_case[0], algorithm.calculate_coins(test_case[1], test_case[2]))

    def _run_canonical_coins(self, algorithm: ChangeAlgorithm):
        test_cases = [
            # expected, coins, amount
            ({}, {1:1}, 0),
            ({1:1}, {1:1}, 1),
            ({1:10}, {1:10}, 10),
            ({2:5}, {2:5}, 10),
            ({2:3, 1:4}, {2:3, 1:10}, 10),
            ({200: 1, 100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1:1}, {200:10, 100:10, 50:10, 20:10, 10:10, 5:10, 2:10, 1:10}, 388)
        ]
        for test_case in test_cases:
            with self.subTest(f"coins: {test_case[1]}, amount: {test_case[2]}"):
                self.assertEqual(test_case[0], algorithm.calculate_coins(algorithm.sort_coins(test_case[1]), test_case[2]))

        exception_test_cases = [
            ({}, 1),
            ({2:1}, 1),
            ({1:1}, 2)
        ]
        for test_case in exception_test_cases:
            with self.subTest(f"coins: {test_case[0]}, amount: {test_case[1]}"):
                self.assertRaises(CalculationError, algorithm.calculate_coins, algorithm.sort_coins(test_case[0]), test_case[1])
