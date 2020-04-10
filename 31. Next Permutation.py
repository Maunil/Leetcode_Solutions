class Solution:
    def swap (self, nums, ind1, ind2):
        nums[ind1] , nums[ind2] = nums[ind2] , nums[ind1]
    
    def reverse(self, nums, begin, end):
        while begin < end:
            self.swap(nums, begin, end)
            begin = begin + 1 
            end = end - 1 
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len (nums)  
        if length == 0 or length == 1:
            return nums 
        
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i+1]:
                self.reverse(nums, i+1, length - 1)
                
                for j in range(i+1, length):
                    if nums[j] > nums[i]:
                        self.swap(nums, j, i)
                        break 
                
                return 
            
        self.reverse(nums, 0, length - 1)
        