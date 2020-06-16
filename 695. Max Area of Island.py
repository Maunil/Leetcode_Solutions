class Solution:
    def dfs_util(self, r, c, N, M, grid, area_count):
        if r < 0 or c < 0 or r >= N or c >= M or grid[r][c] != 1:
            return 
    
        area_count[0] += 1 
        grid[r][c] = -1 
        
        self.dfs_util(r+1,c,N,M,grid, area_count)
        self.dfs_util(r,c+1,N,M,grid, area_count)
        self.dfs_util(r-1,c,N,M,grid, area_count)
        self.dfs_util(r,c-1,N,M,grid, area_count)

        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        N = len(grid)
        if N == 0:
            return 0
        
        M = len(grid[0])
        
        ans = 0 
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    area_count = []
                    area_count.append(0)
                    self.dfs_util(i, j, N, M, grid, area_count)

                    if area_count[0] > ans:
                        ans = area_count[0]

        return ans