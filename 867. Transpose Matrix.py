class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ans = []        
        i, j = 0,0 
        
        for i in range(len(A[0])):
            dummy = []
            for j in range(len(A)): 
                dummy.append(A[j][i])
            
            ans.append(dummy)
            
        return ans