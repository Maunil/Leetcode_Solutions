from heapq import heappush, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1 
            else:
                dic[s[i]] = dic[s[i]] + 1 
            
        s = ""
        heap = []
        
        for key in dic:
            heappush(heap, (dic[key]*-1, key))
        
        
        for i in dic:
                val, key = heappop(heap)
                val = val*-1
                
                while val:
                    s = s + str(key)
                    val = val - 1 
        
        return s 
        
        
        
            