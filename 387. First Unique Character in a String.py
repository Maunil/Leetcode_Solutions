class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s) 
        dic = {}
        
        for i in range(length):
            if s[i] in dic:
                dic[s[i]] = dic[s[i]] + 1  
            else:
                dic[s[i]] = 1 
                
        
        for i in range(length):
            if dic[s[i]] == 1:
                return i 
            
            
        return -1 

                