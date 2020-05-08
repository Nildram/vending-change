from dataclasses import dataclass
from typing import Dict, List

class Change:

    def __init__(self):
        self.initialise({})

    def initialise(self, coins):
        self.coins = dict(sorted(coins.items(), reverse=False))

    def add_coins(self, coins: Dict[int, int]):
        self.coins.update(coins)

    def get_change(self, amount: int) -> List[int]:
        p = self.far(amount)
        print(p)
        #for row in p:
        #    for col in row:
        #        print("{:3.0f}".format(col), end=" ")
        #    print("\n")

        if amount == 0:
            return []

        change = []
        for coin, coin_count in self.coins.items():
            while coin_count and coin <= (amount - sum(change)):
                change.append(coin)
                # Remove coin
                # Check if we're over
                if sum(change) == amount:
                    break

        return change

    def far(self, amount: int) -> List[int]:
        @dataclass
        class Change:
            coins: Dict[int, int]
            number_of_coins: int = float('inf')

            def __init__(self, coins: Dict[int, int]=None):
                self.coins = {} if coins == None else coins
                self.number_of_coins = sum(self.coins.values())
                #self.number_of_coins = self.number_of_coins if self.number_of_coins else float('inf')

            def __add__(self, other):
                coins = {**self.coins, **other.coins}
                for key, value in coins.items():
                    if key in self.coins and key in other.coins:
                        coins[key] = value + self.coins[key]
                            
                return Change(coins)

            def __eq__(self, other) -> bool:
                return self.number_of_coins == other.number_of_coins

            def __lt__(self, other) -> bool:
                return self.number_of_coins < other.number_of_coins

            def __gt__(self, other) -> bool:
                return self.number_of_coins > other.number_of_coins



        dp = [[Change() for x in range(amount+1)] for x in range(len(self.coins))]
        #dp[0][0] = Change()
        print(dp)

        def print_dp(dp):
            for row in dp:
                for col in row:
                    print("{:3.0f}".format(col), end=" ")
                print("\n")

        # TODO create a class for the change rather than a dict or list
        # that way you can use a map for the change, plus a total coins for the matrix

        


        for coin_index, (coin, coin_count) in enumerate(self.coins.items()):
            dp[coin_index] = dp[coin_index-1].copy() # try and use prev row or temporary, can we just switch between two rows overwiting?
            for target_sum in range(coin, amount + 1):
                print(coin, coin_count, coin_index, target_sum, target_sum/coin)
                if int(target_sum/coin) > coin_count:
                    dp[coin_index][target_sum] = coin_count + (dp[coin_index -1][target_sum-coin*coin_count])
                else:
                    print(dp[coin_index][target_sum-coin] + Change({1:1}))
                    dp[coin_index][target_sum] = min(filter(lambda x: x.number_of_coins != 0, (dp[coin_index-1][target_sum], dp[coin_index][target_sum - coin] + Change({coin:1}))))

                
        return dp