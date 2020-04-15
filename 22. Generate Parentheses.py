class Solution:
    def help(self, left, right, curr, n, result):
        if left == n and right == n:
            #Base case valid
            result.append(curr)
            return 
        
        if left < right or left > n:
            return 
        
        self.help(left+1, right, curr + "(", n, result)
        self.help(left, right+1, curr + ")", n, result)
    
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.help(0, 0, "", n, result)
        
        return result
        