class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        full_sum = 0
        actual_sum = 0 
        dic = {}
        
        for i in (nums):
            if i not in dic:
                dic[i] = True
                full_sum = full_sum + i
            
            actual_sum = actual_sum + i
        
        return full_sum*2 - actual_sum 