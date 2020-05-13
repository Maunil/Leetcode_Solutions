class Solution:
    total = None 
    def calculate(self, curr):
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        
        if len(curr) == 1 :
            return 1 
    
        sub_dic = {}
        flag = True 
        for i in range (len(curr)):
            if curr[i] not in sub_dic:
                sub_dic [curr[i]]  = 1 
            else:
                flag = False
                sub_dic [curr[i]]  += 1 
                
        ans = fact[len(curr)] 
        
        if flag == False:
            for k in sub_dic:
                ans = int(ans/fact[sub_dic[k]])
                
        return ans 
    
    def help(self, tiles, curr, index, k, dic):
        if len(curr) == k and curr not in dic:
            dic[curr] = True 
            print (curr)
            print (self.calculate(curr))
            self.total+= self.calculate(curr)            
            return 
        
        for i in range(index, len(tiles)):
            curr = curr + (tiles[i])
            self.help(tiles, curr, i + 1, k, dic)
            curr = curr[:len(curr)-1]
            
    
    def numTilePossibilities(self, tiles: str) -> int:
        self.total = 0 
        tiles = sorted(tiles)
        for i in range(1, len(tiles) + 1):
            dic = {}
            self.help(tiles, "", 0, i, dic)
            
        return self.total 
        