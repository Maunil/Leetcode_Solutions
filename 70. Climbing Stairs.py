class Solution:        
    def sol(self, n, dic) : # Recursion based solutoin 
        if n == 1 or n == 2:
            return n 
        
        if n in dic:
            return dic[n]
        
        dic[n] = self.sol(n - 1, dic) + self.sol(n - 2, dic)
        return dic[n]
    
    def dp_sol(self, n, dic): # DP based solution 
        for i in range(3, n+1): 
            dic[i] = dic[i-2] + dic[i-1]
        
        return dic[n]
    
    def climbStairs(self, n: int) -> int:
        dic = {}
        #return self.sol(n, dic) 
        dic[1] = 1 
        dic[2] = 2 
        
        return self.dp_sol(n, dic)
        
        