class Solution:
    
    def check(self, nums, start, end, target):
        if sum(nums[start:end]) >= target:
            return True 
        
        return False
    
    def subset(self, nums, index, end, curr, limit, target, dummy, dic): 
        key = str(index) + str(curr)
        
        if key in dic:
            return dic[key] 
        
        if curr == target:
            return True 

        if curr > target:
            return 
                    
        for i in range(index, end):
            curr = curr + (nums[i])
            state = self.subset(nums, i+1, end, curr, limit, target, dummy, dic) 
            dic[key] = state 
            
            if state:
                return True 
            curr = curr - nums[i]
    
    
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        length = len(nums)
        
        if length == 1 :
            return False
        
        total = total/2        
        
        dic = {}
        
        if self.subset(nums, 0, length, 0, 0, total, [], dic):
            return True 
        
        return False
                