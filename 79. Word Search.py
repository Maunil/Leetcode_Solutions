class Solution:
    def dfs_helper(self, board, r, c, index, word):
        if index == len(word):
            return True 
                
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[index]:
            return False
    
        temp = board[r][c] 
        board[r][c] = "-1"
        
        if  self.dfs_helper(board, r+1, c, index + 1, word) or self.dfs_helper(board, r-1 , c, index + 1, word) or self.dfs_helper(board, r, c +1 , index + 1, word) or self.dfs_helper(board, r, c-1, index + 1, word):
            return True 
        
        board[r][c] = temp 
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs_helper(board, i, j, 0, word):
                    return True 
        return False 