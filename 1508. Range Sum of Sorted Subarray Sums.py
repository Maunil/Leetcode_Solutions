class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        length = len(nums)
        
        for i in range(length):
            val = nums[i]
            ans.append(val)
            for j in range(i+1, length):
                val += nums[j]
                ans.append(val)
                
        ans.sort()
        return sum(ans[left-1:right]) % (10**9 + 7)
    
        