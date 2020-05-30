class Solution:
    
    def help(self, image, r, c, newcolor, oldcolor):
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != oldcolor:
            return 
        
        image[r][c] = newcolor 
        
        self.help(image, r+1, c, newcolor, oldcolor)
        self.help(image, r, c+1, newcolor, oldcolor)
        self.help(image, r, c-1, newcolor, oldcolor)
        self.help(image, r-1, c, newcolor, oldcolor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:     
        if sr < len(image) and sc < len(image[0]) and newColor == image[sr][sc]:
            return image 
                    
        self.help(image, sr, sc, newColor, image[sr][sc])
        
        return image 