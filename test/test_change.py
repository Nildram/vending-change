import unittest

from change.change import ChangeCalculator

class TestChange(unittest.TestCase):

    default_float = {
        1:10,
        2:10,
        5:10,
        10:10,
        20:10,
        50:10,
        100:10,
        200:10
    }

    non_canonical_float = {

        
        3:1,
        4:10,
        1:6,
        #8:10,
        #12:10,
        #13:10,
        #100:10,
    }
    def setUp(self):
        pass
        self.change = ChangeCalculator()
        self.change.initialise(TestChange.default_float)

    # def test_change(self):
    #     self.change = Change()
    #     self.change.initialise(TestChange.default_float)
    #     self.assertEqual([], self.change.get_change(0))
    #     self.assertEqual([1], self.change.get_change(1))
    #     self.assertEqual([2], self.change.get_change(2))
    #     self.assertEqual([2,1], self.change.get_change(3))
    #     self.assertEqual([2,2], self.change.get_change(4))
    #     self.assertEqual([5], self.change.get_change(5))
    #     self.assertEqual([5,1], self.change.get_change(6))
        # self.assertEqual([5,2], self.change.get_change(7))
        # self.assertEqual([5,2,1], self.change.get_change(8))
        # self.assertEqual([5,2,2], self.change.get_change(9))
        # self.assertEqual([10], self.change.get_change(10))
        # self.assertEqual([10,1], self.change.get_change(11))



    def test_change_2(self):
        self.change = ChangeCalculator()
        self.change.initialise(TestChange.non_canonical_float)
        # self.assertEqual([], self.change.get_change(0))
        # self.assertEqual([1], self.change.get_change(1))
        # self.assertEqual([1,1], self.change.get_change(2))
        # self.assertEqual([3], self.change.get_change(3))
        # self.assertEqual([4], self.change.get_change(4))
        # self.assertEqual([4,1], self.change.get_change(5))
        self.assertEqual({1:2,4:1}, self.change.get_change(6))
        self.change.add_coins({3:1})
        self.assertEqual({3:2}, self.change.get_change(6))
        #self.assertEqual({100:1}, self.change.get_change(100))
        #self.assertEqual({1:1,100:1}, self.change.get_change(101))
    #     self.assertEqual([4,4], self.change.get_change(8))
    #     self.assertEqual([3,3,3], self.change.get_change(9))
    #     self.assertEqual([10], self.change.get_change(10))
    #     self.assertEqual([10,1], self.change.get_change(11))
