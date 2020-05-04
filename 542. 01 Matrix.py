class Solution:
    
    def near_zero(self, matrix, i , j):
        if (i >=0 and i < len(matrix)) and (j >=0 and j < len(matrix[0])) and (matrix[i][j] == float("inf")):
            return True 
        
        return False
                
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = float("inf")
        
                else:
                    q.append([i,j])
        
                    
        while len(q) > 0:
            r, c = q[0]
            q.pop(0)
                    
            if self.near_zero(matrix, r+1, c): 
                matrix[r+1][c] = min(matrix[r+1][c], matrix[r][c] + 1)  
                q.append([r+1, c])
            
            if self.near_zero(matrix, r-1, c): 
                matrix[r-1][c] = min(matrix[r-1][c], matrix[r][c]+ 1)
                q.append([r-1, c])
            
            if self.near_zero(matrix, r, c+1): 
                matrix[r][c+1] = min(matrix[r][c+1], matrix[r][c]+ 1)
                q.append([r, c+1])
            
            if self.near_zero(matrix, r, c -1): 
                matrix[r][c-1] = min(matrix[r][c-1], matrix[r][c]+ 1)
                q.append([r, c-1])
            
            
        return matrix
        
        
        
        
        
                
                
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):         
#                     matrix[i][j] = min(matrix[i][j], self.near_zero(matrix, i-1, j), self.near_zero(matrix, i+1, j), self.near_zero(matrix, i,j-1) ,           self.near_zero(matrix, i, j + 1))
                            
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 matrix[i][j] = min(matrix[i][j],self.near_zero(matrix, i-1, j), self.near_zero(matrix, i+1, j), self.near_zero(matrix, i,j-1) ,           self.near_zero(matrix, i, j + 1))
                            
        
#         return matrix
        
        
                
        
        
        