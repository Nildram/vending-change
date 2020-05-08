from typing import Dict


def combine_coins(existing_coins: Dict[int, int], additional_coins: Dict [int, int]) -> Dict[int, int]:
    coins = {**existing_coins, **additional_coins}
    for key, value in coins.items():
        if key in existing_coins and key in additional_coins:
            coins[key] = value + existing_coins[key]
    return coins


class Change:

    def __init__(self, coins: Dict[int, int]=None):
        self.coins = {} if coins == None else coins
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
        return sum(coin * count for coin, count in self.coins.items())
