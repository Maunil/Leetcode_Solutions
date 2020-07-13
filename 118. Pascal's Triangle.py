class Solution:
    def add_elements(self, ans, level):
        array = []
        array.append(1)
        start = 0 
        
        for i in range(1, len(ans[level])):
            array.append(ans[level][start] + ans[level][i])
            start += 1 
        
        array.append(1)
        ans.append(array)
        
        
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        ans = [[1]]
        if numRows == 1:
            return ans 
        
        ans.append([1,1])
        for i in range(numRows-2):
            self.add_elements(ans, i+1)
            
        return ans 
            
        
        
        
        
        