class Solution:
    left_index = None 
    right_index = None 
        
    def left_binary(self, nums, left, right, target):
        if left <= right:
            mid = left + (right - left) // 2 
            
            if nums[mid] == target:
                if self.left_index > mid:
                    self.left_index = mid 
                return self.left_binary(nums, left, mid-1, target)
                
            elif nums[mid] < target:
                return self.left_binary(nums, mid + 1, right, target)
                
            elif nums[mid] > target: 
                return self.left_binary (nums,left, mid-1, target)
        return 
    
    def right_binary(self, nums, left, right, target):
        if left <= right:
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                if self.right_index < mid:
                    self.right_index = mid 
                return self.right_binary(nums, mid+1, right, target)
                
            elif nums[mid] < target:
                return self.right_binary(nums, mid + 1, right, target)
                
            elif nums[mid] > target: 
                return self.right_binary (nums,left,mid-1, target)
        return 
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        self.left_index = float("+inf") 
        self.right_index = - 1 
        self.left_binary(nums, 0, len(nums)-1, target)

        if self.left_index == float("+inf"):
            return [-1,-1]
        
        self.right_binary(nums, 0, len(nums)-1, target)
        
        return [self.left_index, self.right_index]
        
        