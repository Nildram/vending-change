from typing import Dict, List

from change_calculator.change import Change, combine_coins
from change_calculator.change_algorithm import ChangeAlgorithm
from change_calculator.exceptions import (FloatTooLargeError,
                                          InvalidChangeAmountError,
                                          InvalidCoinError, InvalidCountError)


class ChangeCalculator:

    MAX_COIN_VALUE = 5000
    MAX_FLOAT_VALUE = 10000
    MAX_CHANGE_VALUE = 5000

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
        self._change_algorithm = change_algorithm
        self.initialise({})

    def initialise(self, coins: Dict[int, int]):
        """Initialise with a 'float' of coins.

        Args:
            coins (dict) : Provides the initial 'float' with key being the
                coin denomination and the value being the number of coins
                for that denomination. There is currently a limit of
                5000 for coin denominations and 10000 for total float.

        Raises:
            InvalidCoinError: Raised when a coin with value <= 0 or > max
                value is found in `coins`.
            NegativeCountError: Raised when the count for a coin contains
                a negative value is found in `coins`.
        """
        self._validate_coins(coins)
        self._validate_float({}, coins)
        self._coins = self._change_algorithm.sort_coins(coins)

    def add_coins(self, coins: Dict[int, int]):
        """Add coins to the current 'float'.

        Args:
            coins (dict) : Provides the initial 'float' with key being the
                coin denomination and the value being the number of coins
                for that denomination. There is currently a limit of
                50 for coin denominations and 5000 for total float.

        Raises:
            InvalidCoinError: Raised when a coin with value <= 0 or > max
                value is found in `coins`.
            NegativeCountError: Raised when the count for a coin contains
                a negative value is found in `coins`.
        """
        self._validate_coins(coins)
        self._validate_float(self._coins, coins)
        self._coins = combine_coins(self._coins, coins)
        self._coins = self._change_algorithm.sort_coins(self._coins)

    def get_change(self, amount: int) -> List[int]:
        """Get the optimum change for `amount`.

        Args:
            amount (int): The amount of change to calculate. There is
                currently a limit of 5000 for change.

        Returns:
            dict : The calculates change with key being the coin
                denomination and the value being the number of coins
                for that denomination.

        Raises:
            InvalidCoinError: Raised when the requested amount
                is negative or exceeds max coin value.
            CalculationError: Raised when the requested amount cannot be
                calculated from the given set of coins.
        """
        self._validate_change_amount(amount)
        change = self._change_algorithm.calculate_coins(self._coins, amount)
        self._remove_change(change)
        return change

    def _validate_change_amount(self, amount):
        if amount < 0 or amount > self.MAX_CHANGE_VALUE:
            raise InvalidChangeAmountError()

    def _remove_change(self, change: Dict[int, int]):
        for coin, count in change.items():
            self._coins[coin] -= count

    def _validate_coins(self, coins: Dict[int, int]):
        for coin, count in coins.items():
            if coin <= 0 or coin > self.MAX_COIN_VALUE:
                raise InvalidCoinError()
            elif count < 0:
                raise InvalidCountError()

    def _validate_float(self, existing_coins, additional_coins):
        if self._sum_coins(existing_coins) + self._sum_coins(additional_coins) > self.MAX_FLOAT_VALUE:
            raise FloatTooLargeError()

    def _sum_coins(self, coins: Dict[int, int]) -> int:
        return sum(coin * count for coin, count in coins.items())
