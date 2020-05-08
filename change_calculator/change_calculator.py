from typing import Dict, List

from change_calculator.change import Change, sum_coins
from change_calculator.change_algorithm import ChangeAlgorithm


class ChangeCalculator:

    def __init__(self, change_algorithm: ChangeAlgorithm):
        self.change_algorithm = change_algorithm
        self.initialise({})

    def initialise(self, coins: Dict[int, int]):
        # TODO check for negatives and throw?
        self.coins = self.change_algorithm.sort_coins(coins)

    def add_coins(self, coins: Dict[int, int]):
        self.coins = sum_coins(self.coins, coins)

    def get_change(self, amount: int) -> List[int]:
        # TODO check for negative number and throw?
        return self.change_algorithm.calculate_change(self.coins, amount)