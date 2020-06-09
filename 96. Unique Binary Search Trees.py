class Solution:
    def help(self, dp, n):
        left = 0 
        right = n - 1 
        ans = 0
        
        while n: 
            ans += (dp[left]*dp[right])
            left+=1 
            right-=1 
            n = n - 1 
            
        return ans
    
    def numTrees(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(1)
        dp.append(2)
        
        if n == 0:
            return 0
        
        if n <= 2:
            return dp[n]
        
        for i in range(3, n+1):
            dp.append(self.help(dp, i))
        
        return dp[n]
    
    
                
        