from dataclasses import dataclass
from typing import Dict, List

def print_dp(dp):
    for row in dp:
        for col in row:
            print("{:3.0f}, {}".format(col.number_of_coins, col.coins), end=" ")
        print("\n")

def sum_coins(existing_coins: Dict[int, int], additional_coins: Dict [int, int]) -> Dict[int, int]:
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
        return Change(sum_coins(self.coins, other.coins))

    def __eq__(self, other) -> bool:
        return self.number_of_coins == other.number_of_coins

    def __lt__(self, other) -> bool:
        return self.number_of_coins < other.number_of_coins

    def __gt__(self, other) -> bool:
        return self.number_of_coins > other.number_of_coins 


class ChangeCalculator:

    def __init__(self):
        self.initialise({})

    def initialise(self, coins):
        self.coins = dict(sorted(coins.items(), reverse=False))

    def add_coins(self, coins: Dict[int, int]):
        self.coins = sum_coins(self.coins, coins)

    def get_change(self, amount: int) -> List[int]:
        return self.dynamic(amount)

    def greedy(self, amount: int) -> List[int]:
        change = []
        for coin, coin_count in self.coins.items(): 
            while coin_count and coin <= (amount - sum(change)):
                change.append(coin)
                coin_count -= 1
                if sum(change) == amount: 
                    break

    def dynamic(self, amount: int) -> List[int]: 
        dp = [[Change() for x in range(amount+1)] for x in range(len(self.coins))]        

        def out_of_current_coins(target_sum: int, coin: int, coin_count: int) -> bool:
            return int(target_sum/coin) > coin_count

        def get_valid_change_options(change_options: List[Change]) -> List[Change]:
            return filter(lambda x: x.number_of_coins != 0, change_options)

        def get_most_optimal_change(change1: Change, change2: Change) -> Change:
            return min(get_valid_change_options([change1, change2]))

        def get_change_with_coin_limit(coin, coin_count, dp, target_sum):
            remainder = target_sum - (coin * coin_count)
            remainder_using_previous_coin = dp[coin_index -1][remainder]
            max_change_using_current_coin = Change({coin: coin_count})
            return max_change_using_current_coin + remainder_using_previous_coin

        def get_change_without_coin_limit(coin, dp, target_sum):
            return get_most_optimal_change(
                dp[coin_index][target_sum], 
                dp[coin_index][target_sum - coin] + Change({coin:1}))

        for coin_index, (coin, coin_count) in enumerate(self.coins.items()):
            dp[coin_index] = dp[coin_index-1].copy()
            for target_sum in range(coin, amount + 1):
                #print(coin, coin_count, coin_index, target_sum, target_sum/coin)
                if out_of_current_coins(target_sum, coin, coin_count):
                    dp[coin_index][target_sum] = get_change_with_coin_limit(coin, coin_count, dp, target_sum)
                else:
                    #print(dp[coin_index][target_sum-coin] + Change({1:1}))
                    dp[coin_index][target_sum] = get_change_without_coin_limit(coin, dp, target_sum)

        print_dp(dp)
        return dp[len(self.coins)-1][amount].coins