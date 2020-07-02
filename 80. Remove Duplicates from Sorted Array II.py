class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        valid_counter = 0
        total_elements = 0 
        length = len(nums)
        
        if length == 0:
            return 0
        
        counter +=1 
        valid_counter = 1  
        total_elements +=1 
        
        while counter < length:            
            if nums[counter] == nums[counter-1]:
                if total_elements < 2:
                    nums[valid_counter] = nums[counter]
                    total_elements += 1 
                    valid_counter += 1 
                    
            else:
                total_elements = 0
                nums[valid_counter] = nums[counter]
                total_elements += 1 
                valid_counter += 1
            
            counter += 1 
        
        return valid_counter 