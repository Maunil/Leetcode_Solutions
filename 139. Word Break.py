class Solution:
    def help(self, s, memory, dic):              
        if s == None:
            return True 
        
        if s in memory :
            return memory[s]
        
        if s in dic:
            return True 
        
        for word in dic:
            if s[:len(word)] != word:
                continue
            else:
                memory[s[:len(word)]] = True 
                if self.help(s[len(word):], memory, dic):
                    return True 
        
        memory[s] = False
        return False
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return  self.help(s,{}, wordDict)
        