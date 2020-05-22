class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1) 
        for i in range (1, len(nums)):
            left.append(left[i-1]*nums[i-1])
            
        right = 1
        for i in range(len(nums)-1, -1, -1):
            dummy = right*nums[i]         
            nums[i] = left[i] * right
            right = dummy 
            
        return nums 
            