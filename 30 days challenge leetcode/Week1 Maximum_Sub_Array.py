class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 
        
        sum_con = 0 
        max_sum = None
        
        for i in range(len(nums)):
            sum_con = max(sum_con + nums[i], nums[i])
            
            if max_sum == None or max_sum < sum_con:
                max_sum = sum_con 
                
        return max_sum 
            