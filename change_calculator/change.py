from typing import Dict


def combine_coins(existing_coins: Dict[int, int], additional_coins: Dict[int, int]) -> Dict[int, int]:
    coins = {**existing_coins, **additional_coins}
    for key, value in coins.items():
        if key in existing_coins and key in additional_coins:
            coins[key] = value + existing_coins[key]
    return coins


class Change:

    def __init__(self, coins: Dict[int, int]=None):
        """Represents a set of coin change.

        The class stores both a set of change and total number
        of coins in the change. Comparison is based on the total
        number of coins.

        Args:
            coins: The set of coins that make up the change - key being the
                coin denomination and the value being the number of coins
                for that denomination.
        """
        self.coins = {} if coins is None else coins
        self.number_of_coins = sum(self.coins.values())

    def __add__(self, other):
        return Change(combine_coins(self.coins, other.coins))

    def __eq__(self, other) -> bool:
        return self.number_of_coins == other.number_of_coins

    def __lt__(self, other) -> bool:
        return self.number_of_coins < other.number_of_coins

    def __gt__(self, other) -> bool:
        return self.number_of_coins > other.number_of_coins

    def total(self) -> int:
        """Get the sum of all the change.

        Return:
            int: The sum of all the coins based on denomination
                and count.
        """
        return sum(coin * count for coin, count in self.coins.items())
