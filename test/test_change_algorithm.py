import unittest

from change_calculator.change_algorithm import ChangeAlgorithm

# class TestGreedyAlgorithm(unittest.TestCase):

#     def test_cases(self):
#         algorithm = ChangeAlgorithm.create(canonical_coin_system=True)

#         self.assertEqual({}, algorithm.calculate_change({}, 0))
#         self.assertEqual({}, algorithm.calculate_change({}, 1))
#         self.assertEqual({}, algorithm.calculate_change({2:1}, 1))
#         self.assertEqual({}, algorithm.calculate_change({1:1}, 2))
#         self.assertEqual({1:1}, algorithm.calculate_change({1:1}, 1))
#         self.assertEqual({1:10}, algorithm.calculate_change({1:10}, 10))
#         self.assertEqual({2:5}, algorithm.calculate_change({2:5}, 10))
#         self.assertEqual({2:3, 1:4}, algorithm.calculate_change({2:3, 1:10}, 10))
#         self.assertEqual({200: 1, 100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1:1}, algorithm.calculate_change({200:10, 100:10, 50:10, 20:10, 10:10, 5:10, 2:10, 1:10}, 388))

class TestDynamicProgrammingAlgorithm(unittest.TestCase):

    def test_cases(self):
        algorithm = ChangeAlgorithm.create(canonical_coin_system=False)

        self.assertEqual({}, algorithm.calculate_change({}, 0))
        self.assertEqual({}, algorithm.calculate_change({}, 1))
        self.assertEqual({}, algorithm.calculate_change({2:1}, 1))
        self.assertEqual({}, algorithm.calculate_change({1:1}, 2))
        self.assertEqual({1:1}, algorithm.calculate_change({1:1}, 1))
        self.assertEqual({1:10}, algorithm.calculate_change({1:10}, 10))
        self.assertEqual({2:5}, algorithm.calculate_change({2:5}, 10))
        self.assertEqual({2:2, 1:2}, algorithm.calculate_change({1:10, 2:2}, 6))
        self.assertEqual({1:1, 2:1, 5:1, 10:1, 20:1, 50:1, 100:1, 200:1}, algorithm.calculate_change({1:10, 2:10, 5:10, 10:10, 20:10, 50:10, 100:10, 200:10}, 388))

        self.assertEqual({3:2}, algorithm.calculate_change({1:10, 3:2}, 6))
        self.assertEqual({1:3, 3:1}, algorithm.calculate_change({1:10, 3:1}, 6))
        self.assertEqual({3:2}, algorithm.calculate_change({1:10, 3:2, 4:2}, 6))
        self.assertEqual({1:2, 4:1}, algorithm.calculate_change({1:10, 3:1, 4:2}, 6))
        self.assertEqual({3:1, 65:2, 129:1}, algorithm.calculate_change({1:10, 3:10, 5:10, 9:10, 17:10, 33:10, 65:10, 129:10}, 262))
        self.assertEqual({}, algorithm.calculate_change({1:1, 3:10}, 5))
        self.assertEqual({1:1, 3:1, 5:1}, algorithm.calculate_change({1:1, 3:1, 5:1}, 9))
        self.assertEqual({1: 1, 3: 1, 5: 1, 9: 1, 17: 1, 33: 1, 65: 1, 129: 1}, algorithm.calculate_change({1:1, 3:1, 5:1, 9:1, 17:1, 33:1, 65:1, 129:1}, 262))
