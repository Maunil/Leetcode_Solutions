import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for i in nums[k:]:
            if i > h[0]:
                heapq.heapreplace(h, i)
        
        return h[0]    
        
        
#         nums = [int(i)*-1 for i in nums]
#         heapq.heapify(nums) 
        
#         for i in range(k-1):
#             heapq.heappop(nums)
            
#         return heapq.heappop(nums)*-1
            