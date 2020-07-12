class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        length = len(arr)
        if length == 0:
            return 0 
        
        n_chunks = 0 
        i = 0

        while i < length:
            if arr[i] == i:
                n_chunks += 1
                i+=1 
            else:
                ref = arr[i] 
                while i <= ref:
                    if arr[i] > ref:
                        ref = arr[i]
                    i+=1 
                
                n_chunks +=1
                    
        return n_chunks 
    
                
                