class Solution:
    def binary(self, nums, left, right, target):
        if left <= right:
            mid = left + (right - left) // 2 
                
            if nums[mid] == target:
                return mid 
            
            elif (nums[left] < nums[mid]):
                if nums[left] <= target<= nums[mid]: 
                    return self.binary(nums, left, mid , target)
                else:
                    return self.binary(nums, mid+1, right, target)
                    
            elif left != right:
                if nums[mid+1] <= target <= nums[right] : 
                    return self.binary(nums, mid+1, right , target)
                else:
                    return self.binary(nums, left, mid, target)
                
                
        return -1 
    
    def search(self, nums: List[int], target: int) -> int: 
        if len(nums) == 0:
            return -1 
        
        return self.binary(nums, 0, len(nums)-1, target)
        