class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        dic = {}
        
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1 
        
        for key in dic:
            if len(h) < k:
                heapq.heappush(h, (dic[key], key))
            elif h[0][0] < dic[key]:
                heapq.heappop(h)
                heapq.heappush(h, (dic[key], key))
            
            
        return [h.pop()[1] for i in range(len(h))]