class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def dfs(self, i,j, rooms, track):
        #Conditions to stop 
        
        if (i < 0 or i >= len(rooms) or j < 0 or j>=len(rooms[0]) or rooms[i][j] < track):
            return 
        
        rooms[i][j] = track
        self.dfs(i-1, j, rooms, track+1)
        self.dfs(i+1, j, rooms, track+1)
        self.dfs(i, j-1, rooms, track+1)
        self.dfs(i, j+1, rooms, track+1)
        
    def wallsAndGates(self, rooms):
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(i, j, rooms, 0)
                
        return rooms


'''
BFS Approch
'''

import math 
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    MAX_INT = math.pow(2,31) -1 
    def condition_check (self, i, j, rooms):
        if (i < 0 or i >= len(rooms) or j < 0 or j>=len(rooms[0]) or rooms[i][j] !=  self.MAX_INT):
            return False
            
        return True 
        
    def bfs_util(self, rooms):
        Q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    Q.append([i,j])
                    
        levels = 1 
        while Q:
            n = len(Q)
            while n:
                r, c = Q[0][0], Q[0][1]
                if self.condition_check(r+1, c, rooms):
                    Q.append([r+1, c])
                    rooms[r+1][c] = levels
                    
                if self.condition_check(r, c+1, rooms):
                    Q.append([r, c+1])
                    rooms[r][c+1] = levels
                    
                if self.condition_check(r-1, c, rooms):
                    Q.append([r-1, c])
                    rooms[r-1][c] = levels
                    
                if self.condition_check(r, c-1, rooms):
                    Q.append([r, c-1])
                    rooms[r][c-1] = levels
                    
                Q.pop(0)
                n = n - 1
                
            levels+=1 
        
        return rooms

    def wallsAndGates(self, rooms):
        return self.bfs_util(rooms)
        

