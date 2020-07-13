class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates_ = []
        
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                duplicates_.append(abs(nums[i]))
            else:            
                nums[abs(nums[i])-1] = nums[abs(nums[i])-1] * -1  
            
        
        return duplicates_