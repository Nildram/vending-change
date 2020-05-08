from typing import Dict, List

from change.change import Change, sum_coins
from change.change_algorithm import ChangeAlgorithm


class ChangeCalculator:

    def __init__(self, change_algorithm: ChangeAlgorithm):
        self.change_algorithm = change_algorithm
        self.initialise({})

    def initialise(self, coins: Dict[int, int]):
        self.coins = dict(sorted(coins.items(), reverse=False))

    def add_coins(self, coins: Dict[int, int]):
        self.coins = sum_coins(self.coins, coins)

    def get_change(self, amount: int) -> List[int]:
        return self.change_algorithm.calculate_change(self.coins, amount)