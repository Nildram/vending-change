from typing import Dict, List

from change_calculator.change import Change, combine_coins
from change_calculator.change_algorithm import ChangeAlgorithm
from change_calculator.exceptions import (NegativeChangeAmountError,
                                          NegativeCoinError,
                                          NegativeCountError)


class ChangeCalculator:

    def __init__(self, change_algorithm: ChangeAlgorithm):
        """Interface for calculating change for a specified amount.

        This class provides a way to calculate change for a specified
        amount, given a limited 'float' of existing coins.

        An initial 'float' can be provided using the `initialise` method
        and added to using the `add` method.

        Change can be obtained using the `get_change` method.

        Args:
            change_algorithm (ChangeAlgorithm): The algorithm to use for
                calculating the change.
        """
        self.change_algorithm = change_algorithm
        self.initialise({})

    def initialise(self, coins: Dict[int, int]):
        """Initialise with a 'float' of coins.

        Args:
            coins (dict) : Provides the initial 'float' with key being the
                coin denomination and the value being the number of coins
                for that denomination.

        Raises:
            NegativeCoinError: Raised when a coin with a negative value is
                found in `coins`.
            NegativeCountError: Raised when the count for a coin contains
                a negative value is found in `coins`.
        """
        self._validate_coins(coins)
        self.coins = self.change_algorithm.sort_coins(coins)

    def add_coins(self, coins: Dict[int, int]):
        """Add coins to the current 'float'.

        Args:
            coins (dict) : Provides the initial 'float' with key being the
                coin denomination and the value being the number of coins
                for that denomination.

        Raises:
            NegativeCoinError: Raised when a coin with a negative value is
                found in `coins`.
            NegativeCountError: Raised when the count for a coin contains
                a negative value is found in `coins`.
        """
        self._validate_coins(coins)
        self.coins = combine_coins(self.coins, coins)
        self.coins = self.change_algorithm.sort_coins(coins)

    def get_change(self, amount: int) -> List[int]:
        """Get the optimum change for `amount`.

        Args:
            amount (int): The amount of change to calculate.

        Returns:
            dict : The calculates change with key being the coin
                denomination and the value being the number of coins
                for that denomination.
        """
        if amount < 0:
            raise NegativeChangeAmountError()
        return self.change_algorithm.calculate_coins(self.coins, amount)

    def _validate_coins(self, coins: Dict[int, int]):
        for coin, count in coins.items():
            if coin < 0:
                raise NegativeCoinError()
            elif count < 0:
                raise NegativeCountError()
