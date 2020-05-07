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
        for row in p:
            for col in row:
                print("{:3.0f}".format(col), end=" ")
            print("\n")

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
        dp = [[float('inf') for x in range(amount+1)] for x in range(len(self.coins))]
        dp[3][0] = 0
        print(dp)

        def print_dp(dp):
            for row in dp:
                for col in row:
                    print("{:3.0f}".format(col), end=" ")
                print("\n")

        for coin_index, (coin, coin_count) in enumerate(self.coins.items()):
            dp[coin_index] = dp[coin_index-1].copy() # try and use prev row or temporary, can we just switch between two rows overwiting?
            for target_sum in range(coin, amount + 1):
                print(coin, coin_count, coin_index, target_sum, target_sum/coin)
                if int(target_sum/coin) > coin_count:
                    dp[coin_index][target_sum] = coin_count + (dp[coin_index -1][target_sum-coin*coin_count])
                else:
                    dp[coin_index][target_sum] = min(dp[coin_index-1][target_sum], dp[coin_index][target_sum - coin] + 1)
                
        return dp