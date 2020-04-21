class Solution:
    def help(self, result, target, curr, candidates, index):
        total = sum(curr)
        # Base case 
        if total == target:
            result.append (list(curr))
            return 
        
        # Stop case 
        if total > target:
            return 
        
        for i in range(index, len(candidates)):
            curr.append(candidates[i])
            self.help(result, target, curr, candidates, i)
            curr.pop() 
            
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.help(result, target, [], candidates, 0)
        return result 