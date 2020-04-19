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
    