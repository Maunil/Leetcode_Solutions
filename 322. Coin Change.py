class Solution:
    def assignment(self, coin, dp, index):
        min_coins = float("inf")
        for i in range(len(coin)):
            if index - coin[i] > 0 and dp[index - coin[i]] > 0:
                min_coins = min(min_coins, dp[index-coin[i]] + 1)
                
        return min_coins     
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0 
        
        dp = []
        coins.sort()
        if coins[0] > amount:
            return -1 
        
        for i in range(amount+1):
            dp.append(0)
                
        for i in range(len(coins)):
            if coins [i] <= amount:
                dp[coins[i]] = 1 
                
        for i in range(coins[0]+1, amount + 1):
            if dp[i] == 0:
                min_coins = self.assignment(coins, dp, i) 
                if min_coins != float("inf"):
                    dp[i] = min_coins
        
        if dp[amount] ==0 :
            return -1 
        
        return dp[amount] 
                