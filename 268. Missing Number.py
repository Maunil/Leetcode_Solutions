class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        zero_check = False 
        
        for i in range (length):
            if nums[i] >= length:
                nums[i] = float("inf")
        
        for i in range(length):
            if abs(nums[i]) == float("inf"):
                continue 
            
            if nums[abs(nums[i])] >= 0:
                if nums[abs(nums[i])] == 0:
                    zero_check = True
                    
                nums[abs(nums[i])] = nums[abs(nums[i])] *-1 
                
        for i in range(length):
            if nums[i] > 0:
                return i
            elif nums[i] == 0 and zero_check == False:
                return i
            
        return length  