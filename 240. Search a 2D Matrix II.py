class Solution:    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row = len(matrix) - 1 
        if row == -1:
            return False 
        
        r = 0
        c = len(matrix[0]) - 1  
        if c == -1 :
            return False 
        
        while r <= row and c>=0:
            if matrix[r][c] == target:
                return  True 
            
            elif matrix[r][c] < target:
                r = r + 1 
            
            else:
                c = c - 1 
                
                
        return False
            
                
            