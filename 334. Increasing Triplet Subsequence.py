class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False 
                
        small = nums[0]
        second_small = None
        
        for i in range(1, len(nums)):
            if nums[i] < small:
                small = nums[i]
                
            elif second_small != None and nums[i] > second_small:
                return True 

            elif nums[i] > small:
                second_small = nums[i]
            
        return False 