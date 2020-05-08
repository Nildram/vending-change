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
        self.assertEqual({2:5}, algorithm.calculate_change({2:5, 10:10}, 10))
        

# class TestDynamicProgrammingAlgorithm(unittest.TestCase):

#     initial_float = {
#         3:1,
#         4:10,
#         1:6,
#         #8:10,
#         #12:10,
#         #13:10,
#         #100:10,
#     }

#     def setUp(self):
#         pass
#         self.change = ChangeCalculator(ChangeAlgorithm.create(False))
#         self.change.initialise(TestChange.default_float)