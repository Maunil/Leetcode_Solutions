class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return  1 
            
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = float("+inf")
        
        for i in range(N):
            if nums[i] == 0 or abs(nums[i]) > N :
                continue
            elif nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * -1
            
        for i in range(N):
            if nums[i] > 0:
                return i + 1
        
        return N + 1
    
            
        
            
            
        