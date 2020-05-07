from typing import Dict, List

class Change:

    def __init__(self):
        self.initialise({})

    def initialise(self, coins):
        self.coins = dict(sorted(coins.items(), reverse=False))

    def add_coins(self, coins: Dict[int, int]):
        self.coins.update(coins)

    def get_change(self, amount: int) -> List[int]:
        print(self.far(amount))
        if amount == 0:
            return []

        # Recursion will mlet me backtrack to find all other solutions 
        # in the tree
        change = []
        for coin, coin_count in self.coins.items():
            while coin_count and coin <= (amount - sum(change)):
                change.append(coin)
                # Remove coin
                # Check if we're over
                if sum(change) == amount:
                    break

        #return change


        dp = [float('inf')] * (amount + 1)
        dps = [float('inf')] * (amount + 1)
        dp[0] = 0
        dps[0] = 0

        for coin, coin_count in self.coins.items():
            used = 0
            for target_sum in range(coin, amount + 1):
                res = min(dp[target_sum], dp[target_sum - coin] + 1)
                if res < dp[target_sum-1]:
                    used += 1
                if used > coin_count:
                    dp[target_sum] = used-1 + 3 #dp[coin_index -1][target_sum-coin]
                else:
                    dp[target_sum] = res

                #print(dp, used)
                #print("bar",coin)
                dps[target_sum] = coin

        partial_sum = 0
        ndp = [float('inf')] * (amount + 1)
        ndp[0] = 0
        for coin, count in self.coins.items():
            partial_sum += coin * count
            print(partial_sum, coin, count)
            for x in range(coin, min(partial_sum, amount+1)):
                ndp[x] = min(dp[x], dp[x - coin] + 1)


        #print(dp, ndp)
        return change

    def far(self, amount: int) -> List[int]:
        dp = [[float('inf') for x in range(amount+1)] for x in range(len(self.coins))]
        dp[1][0] = 0
        dp[0][0] = 0
        print(dp)

        for coin_index, (coin, coin_count) in enumerate(self.coins.items()):
            for target_sum in range(coin, amount + 1):
                print(coin, coin_count, coin_index, target_sum)
                if target_sum/coin > coin_count:
                    dp[coin_index][target_sum] = coin_count + (dp[coin_index -1][target_sum-coin])
                else:
                    dp[coin_index][target_sum] = min(dp[coin_index-1][target_sum], dp[coin_index][target_sum - coin] + 1)

                print(dp)
                
        return dp


    def bar(self, amount: int) -> List[int]:
        C = [float('inf')] * (amount+1)
        S = [float('inf')] * (amount+1)
        C[0] = 0
        S[0] = 0

        # for coin, coin_count in self.coins.items():
        #     for _ in range(coin_count):
        #         index = 0
        #         while index < len(C) and C[index] != float('inf'):
        #             print("foo", index, coin, len(C))
        #             if index+coin < len(C) and C[index]+1 < C[index+coin]:
        #                 C[index+coin] = C[index]+1
        #                 S[index+coin] = coin
        #             index += 1
        for coin, coin_limit in self.coins.items():
            if coin_limit <= 0:
                continue
            for index in range(0, amount + 1 - coin):
                print("foo", coin, coin_limit, index, C[index])
                if C[index]+1 < C[index+coin]:
                    C[index+coin] = C[index]+1
                    S[index+coin] = coin
                    coin_limit -= 1
                    print("removing")
                    if coin_limit <= 0:
                        break

        return C, S

    
    # def jar(self, amount: int) -> List[int]:
    #     public static void coinChange(int max_value, int coins[], int count[]) {

    #     int coins_sz = coins.length;
    #     int dp[] = new int[max_value + 1];

    #     Arrays.fill(dp, Integer.MAX_VALUE);
    #     dp[0] = 0;
    #     int partial_sum = 0;
    #     for (int i = 0; i < coins_sz; i++) 
    #     {
    #         partial_sum += coins[i] * count[i];
    #         for (int j = coins[i]; j <= partial_sum && j <= max_value; j++) 
    #         {
    #             dp[j] = Math.min(dp[j - coins[i]] + 1, dp[j]);
    #             sp[j] = coin
    #         }
    #     }
    #     for (int i = 1; i <= max_value; i++) {
    #         System.out.println("Coin value = " + i
    #         + ", Minimum number of coins = " + dp[i]);
    #     }   
    #     }


    # def car(self, amount: int) -> List[int]:
    #     dp = [[len(self.coins)] for x in range(amount+1)]

    #     result = 0
    #     for amount_index in range(1, amount):
    #         for coin_index in range(1, len(self.coins)):
    #             for coin_count in range(1, self.coins.items):
    #                 if amount_index > self.coins[coin_index] * coin_count:
    #                     dp[amount_index][coin_index] += dp[amount_index - self.coins[coin_index] * coin_count][coin_index]
    #                 if amount_index == self.coins[coin_index] * coin_count:
    #                     dp[amount_index][coin_index] += 1
        
    #     print(dp)
    # public static int countWays(int[] coins, int[] count, int sum) {

	# 	int n = coins.length;
	# 	int[][] dp = new int[sum + 1][n + 1];

	# 	int ret = 0;
	# 	for (int i = 1; i <= sum; i++) {
	# 		for (int j = 1; j <= n; j++) {
	# 			for (int k = 1; k <= count[j - 1]; k++) {
	# 				if (i > coins[j - 1] * k)
	# 					dp[i][j] += dp[i - coins[j - 1] * k][j - 1];

	# 				if (i == coins[j - 1] * k)
	# 					dp[i][j] += 1;

	# 			}
	# 		}
	# 	}
	# 	for (int i = 0; i <= n; i++) {
	# 		ret += dp[sum][i]; 
	# 	}
	# 	return ret;
	# }