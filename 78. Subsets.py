class Solution:
    def help(self, index, nums, end, result, curr, limit):
        if len(curr) == limit:
            result.append(list(curr))
            return 
        
        for i in range(index, end):
            curr.append(nums[i])
            self.help(i + 1, nums, end, result, curr, limit)
            curr.pop()
            
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        for i in range(length + 1):
            self.help(0, nums, length, result, [], i)
        
        return result 
        
        