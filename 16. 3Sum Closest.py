class Solution:
    
    def check_iteration(self, diff, nums, i, target):
        lowest_triplet_sum = nums[i] + nums[i+1] + nums[i+2]
        if lowest_triplet_sum > target and diff < abs(lowest_triplet_sum - target):
            return True 
        
        return False
        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = None
        diff = float("inf")
        nums.sort()
        
        for i in range(len(nums) -2):
            left = i+1
            right = len(nums) - 1
            
            if self.check_iteration(diff, nums, i, target):
                return ans
            
            while left < right :
                triplet_sum = nums[i] + nums[left] + nums[right]                
                if triplet_sum == target:
                    return target
                
                elif triplet_sum > target:
                    right -= 1 
                
                else:
                    left += 1
                
                if diff > abs(triplet_sum -target):
                    diff = abs(triplet_sum -target)
                    ans = triplet_sum 
                    
        return ans 
                
        
        
    