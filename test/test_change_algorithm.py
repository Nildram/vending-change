import unittest

from change_calculator.change_algorithm import ChangeAlgorithm

class TestGreedyAlgorithm(unittest.TestCase):

    def test_sort(self):
        algorithm = ChangeAlgorithm.create(canonical_coin_system=True)
        self.assertEqual({}, algorithm.sort_coins({}))
        self.assertEqual({1:1}, algorithm.sort_coins({1:1}))
        self.assertEqual({1:1, 2:1}, algorithm.sort_coins({2:1, 1:1}))
        self.assertEqual({1:1, 3:1, 2:1}, algorithm.sort_coins({3:1, 2:1, 1:1}))

    def test_cases(self):
        algorithm = ChangeAlgorithm.create(canonical_coin_system=True)
        self.assertEqual({}, algorithm.calculate_change({}, 0))
        self.assertEqual({}, algorithm.calculate_change({}, 1))
        self.assertEqual({}, algorithm.calculate_change({2:1}, 1))
        self.assertEqual({}, algorithm.calculate_change({1:1}, 2))
        self.assertEqual({1:1}, algorithm.calculate_change({1:1}, 1))
        self.assertEqual({1:10}, algorithm.calculate_change({1:10}, 10))
        self.assertEqual({2:5}, algorithm.calculate_change({2:5}, 10))
        self.assertEqual({2:2, 1:2}, algorithm.calculate_change({2:2, 1:10}, 6))
        self.assertEqual({200: 1, 100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1}, algorithm.calculate_change({200:10, 100:10, 50:10, 20:10, 10:10, 5:10, 2:10, 1:10}, 387))             

# class TestDynamicProgrammingAlgorithm(unittest.TestCase):

#     def setUp(self):
#         pass
#         self.change = ChangeCalculator(ChangeAlgorithm.create(False))
#         self.change.initialise(TestChange.default_float)