class Solution(object):
    def coinChange(self, coins, amount):
        dp = [10**6] * (10**4 + 1)
        dp[0] = 0
        coins.sort(reverse=True)

        for c in coins:
            if c <= 10**4:
                dp[c] = 1
        
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
            
        return dp[amount] if dp[amount] != 10**6 else -1

