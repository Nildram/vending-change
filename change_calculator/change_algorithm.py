from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, List

from change_calculator.change import Change
from change_calculator.exceptions import CalculationError


def print_dp(dp):
    for row in dp:
        for col in row:
            print("{:3.0f}, {}".format(col.number_of_coins, col.coins), end=" ")
        print("\n")


class ChangeAlgorithm(ABC):
    """Calculates the coins that make up a specified.

    Given a limited number of coins of various denominations,
    the class will provide the optimum number of those coins
    that make up a specifies sum.

    The class also provides a simple static factory method for
    creating new instances of it's subclasses.
    """

    @staticmethod
    def create(canonical_coin_system: bool):
        """Simple static factory method for creating instances.

        Args:
            canonical_coin_system (bool): Set to True if the coin
                system being used is considered canonical, else False.

        Returns:
            ChangeAlgorithm: An instance of a ChangeAlgorithm class
                that is optimum for calculating sums for the coin
                system indicated by `canonical_coin_system`.
        """
        return GreedyAlgorithm() if canonical_coin_system else DynamicProgrammingAlgorithm()

    @abstractmethod
    def calculate_coins(self, coins: Dict[int, int], amount: int) -> Dict[int, int]:
        """Calculate the coins that make up `amount` from `coins`.

        Args:
            coins (dict) : Provides a limited set of coins to calculate the
                `amount` with. The key represents the coin denomination and the
                value represents the number of coins for that denomination.

        Returns:
            dict: The set of coins that make up `amount`. The key represents
                the coin denomination and the value represents the number of
                coins for that denomination.

        Raises:
            CalculationError: Raised when the requested amount cannot be
                calculated from the given set of coins.
        """
        pass

    @abstractmethod
    def sort_coins(self, coins: Dict[int, int]) -> Dict[int, int]:
        pass


class GreedyAlgorithm(ChangeAlgorithm):

    def sort_coins(self, coins: Dict[int, int]) -> Dict[int, int]:
        return dict(sorted(coins.items(), reverse=True))

    def calculate_coins(self, coins: Dict[int, int], amount: int) -> Dict[int, int]:
        self._reset()
        for coin, coin_count in coins.items():
            while coin_count and coin <= (amount - self.change_sum):
                self._update_change(coin, coin_count)
                if self.change_sum == amount:
                    return self.change
                coin_count -= 1

        if amount != 0:
            raise CalculationError()
        return {}

    def _reset(self):
        self.change_sum = 0
        self.change = defaultdict(int)

    def _update_change(self, coin: int, coin_count: int):
        self.change_sum += coin
        self.change[coin] += 1


class DynamicProgrammingAlgorithm(ChangeAlgorithm):

    DP_ROWS = 2

    def sort_coins(self, coins: Dict[int, int]) -> Dict[int, int]:
        return dict(sorted(coins.items(), reverse=False))

    def calculate_coins(self, coins: Dict[int, int], amount: int) -> Dict[int, int]:
        self._reset(coins, amount)

        result = self._do_calculation(amount)
        # print_dp(self.dp)
        if result == {} and amount != 0:
            raise CalculationError()
        return result

    def _do_calculation(self, amount):
        for coin_index, (coin, coin_count) in enumerate(self.coins.items()):
            self.dp[coin_index % self.DP_ROWS] = self.dp[(coin_index-1) % self.DP_ROWS].copy()
            for current_sum in range(coin, amount + 1):
                self._update_dp_array(current_sum, coin, coin_count, coin_index)
        return self.dp[(len(self.coins)-1) % self.DP_ROWS][amount].coins if self.coins else {}


    def _update_dp_array(self, target_sum: int, coin: int, coin_count: int, coin_index: int):
        if self._out_of_current_coins(target_sum, coin, coin_count):
            self.dp[coin_index % self.DP_ROWS][target_sum] = \
                self._get_change_with_coin_limit(coin, coin_count, target_sum, coin_index)
        else:
            self.dp[coin_index % self.DP_ROWS][target_sum] = \
                self._get_change_without_coin_limit(coin, target_sum, coin_index)

    def _reset(self, coins, amount):
        self.coins = coins
        self.dp = [[Change() for x in range(amount+1)] for x in range(self.DP_ROWS)]

    def _out_of_current_coins(self, target_sum: int, coin: int, coin_count: int) -> bool:
        return target_sum/coin > coin_count

    def _get_change_with_coin_limit(self, coin: int, coin_count: int, target_sum: int, coin_index: int) -> Change:
        # This could be optimised to check if the remainder is 0 and returning Change({})
        # at that point rather than checking the sum after adding the current coin. the current solution
        # reads clearer, I think. A similar optimisation could be used in _get_change_without_coin_limit.
        change = self._max_change_using_current_coin(coin, coin_count) + \
            self._remainder_using_previous_coin(coin, coin_count, target_sum, coin_index)
        return Change() if change.total() < target_sum else change

    def _get_change_without_coin_limit(self, coin: int, target_sum: int, coin_index: int) -> Change:
        change = self._get_most_optimal_change(
            self.dp[coin_index % self.DP_ROWS][target_sum],
            self.dp[coin_index % self.DP_ROWS][target_sum - coin] + Change({coin: 1}))
        return Change() if change.total() < target_sum else change

    def _max_change_using_current_coin(self, coin: int, coin_count: int) -> Change:
        return Change({coin: coin_count})

    def _remainder_using_previous_coin(self, coin: int, coin_count: int, target_sum: int, coin_index: int) -> Change:
        remainder = target_sum - (coin * coin_count)
        return self.dp[(coin_index - 1) % self.DP_ROWS][remainder]

    def _get_most_optimal_change(self, change1: Change, change2: Change) -> Change:
        return min(self._get_valid_change_options([change1, change2]))

    def _get_valid_change_options(self, change_options: List[Change]) -> List[Change]:
        return filter(lambda x: x.number_of_coins != 0, change_options)
