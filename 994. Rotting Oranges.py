class Solution:
    def help(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >=len(grid[0]) or grid[row][col] == 2 or grid[row][col] == 0:
            return False

        return True 
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0 
        Q = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    Q.append([i,j]) 
        
        while Q:
            n = len(Q)
            while n:
                row, col = Q[0]
                Q.pop(0) 
                
                if self.help(row + 1, col , grid):
                    grid[row+1][col] = 2 
                    Q.append([row + 1, col])
                if self.help(row , col+1,   grid):
                    grid[row] [col+1 ] = 2
                    Q.append([row, col+1])
                if self.help(row, col-1, grid):
                    grid[row][col-1] = 2
                    Q.append([row, col-1])
                if self.help(row - 1, col , grid):
                    grid[row-1][col] = 2
                    Q.append([row -1, col])

                n -= 1 
                
            minutes += 1

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                           return -1 
        
        if minutes == 0:
            return minutes
        
        return minutes - 1 