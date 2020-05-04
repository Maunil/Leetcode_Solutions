class Solution:
    
    def help(self, image, i , j, color, visit, s_val):
        if (i<0 or i>=len(image)) or (j<0 or j>=len(image[0])) or visit[i][j] == True or image[i][j] != s_val:
            return 
        
        image[i][j] = color    
        visit[i][j] = True 
            
        self.help(image, i, j + 1, color, visit, s_val)
        self.help(image, i, j - 1, color, visit, s_val)
        self.help(image, i+1, j, color, visit, s_val)
        self.help(image, i-1, j, color, visit, s_val)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visit = []
        for i in range(len(image)):
            dummy = []
            for j in range(len(image[0])):
                dummy.append(False)
        
            visit.append(dummy)
            
        self.help(image, sr, sc, newColor, visit, image[sr][sc])
        return image 
                    
                
        