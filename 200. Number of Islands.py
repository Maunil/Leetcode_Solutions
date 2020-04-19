class Solution:
    def dfs(self, i, j , grid, flag):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0" or flag[i][j] == True:
            return 
        
        flag[i][j] = True 
        
        self.dfs(i-1,j, grid, flag)
        self.dfs(i+1,j, grid, flag)
        self.dfs(i,j-1, grid, flag)
        self.dfs(i,j+1, grid, flag)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        flag = []
        number_of_unique = 0 
        for i in range(len(grid)):
            dummy = []
            for j in range(len(grid[0])):
                dummy.append(False)
            
            flag.append(dummy)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j] == "1" and flag[i][j] == False:
                    number_of_unique =  number_of_unique + 1 
                    self.dfs(i,j, grid, flag)
        
        return number_of_unique