class Solution:
    def help(self, r, c, matrix, ans, r_end, c_end):        
        if r < r_end and c < c_end:        
            for i in range(c, c_end):
                ans.append(matrix[r][i])
                matrix[r][i] = float("inf")

            for i in range(r+1, r_end):
                ans.append(matrix[i][c_end-1])
                matrix[i][c_end -1] = float("inf")

            for i in range(c_end-2, c-1 ,-1):
                if matrix[r_end-1][i] != float("inf"):
                    ans.append(matrix[r_end-1][i])

            for i in range(r_end-2, r ,-1):
                if matrix[i][c] != float("inf"):
                    ans.append(matrix[i][c])
            
            return True 
        
        return False 
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        r_end = len(matrix)
        if r_end == 0:
            return ans 
        
        c_end = len(matrix[0])
        r = 0 
        c = 0 

        while self.help(r, c, matrix, ans, r_end, c_end):
            r +=1
            c +=1
            r_end -=1
            c_end -=1
        
        return ans 