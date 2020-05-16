class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        
        for w in words:
            if w not in dic:
                dic[w] = 1 
            else:
                dic[w] += 1 
                
        
        heap = [(-dic[w], w) for w in dic]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]