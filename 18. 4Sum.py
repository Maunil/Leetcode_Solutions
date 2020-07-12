class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        if length < 4 or nums[0] > target and nums[0] > 0:
            return []
        
        ans = set()
        for i in range(length-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue 
                
            for j in range(i+1, length-2):                
                left = j+1
                right = length - 1 
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left +=1 
                        right -= 1 
                        
                    elif total < target:
                        left += 1 
                    
                    else:
                        right -= 1 
                        
        return ans 
                