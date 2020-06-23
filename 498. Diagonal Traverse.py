class Solution:
    def condition_check(self, r,c,row, col):
        if r >= row or c >= col or c < 0 or r < 0:            
            return False
        
        return True 
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        
        ans = []
        flag = True 
        
        row = len(matrix) 
        col = len(matrix[0])
        r, c = 0,0
        flag = False
        while r < row and c < col:    
            if flag:
                while self.condition_check(r,c,row, col):
                    ans.append(matrix[r][c])
                    r += 1
                    c -= 1
                
                r = r - 1
                c = c + 1
                
                if r < row - 1:
                    r += 1
                else:
                    c += 1 
                flag = False
            else:
                while self.condition_check(r,c,row, col):
                    ans.append(matrix[r][c])
                    r -= 1
                    c += 1
                r+= 1
                c-=1 
                if c < col - 1:
                    c += 1
                else:
                    r += 1 
                flag = True        
        
        return ans