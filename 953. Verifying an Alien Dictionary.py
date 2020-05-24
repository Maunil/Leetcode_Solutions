class Solution:
    def comparision(self, word1, word2, alpha):
        length = len(word1)     #min(len(word1), len(word2))
        for i in range(length):
            if i >= len(word2):
                return True 
            elif alpha[word1[i]] < alpha[word2[i]]: 
                return False 
            elif alpha[word1[i]] > alpha[word2[i]]:
                return True 
            
        return False 
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha_dic = {}
        
        for i in range(len(order)):
            alpha_dic[order[i]] = i 
            
        for i in range(1, len(words)):
            if self.comparision(words[i-1], words[i], alpha_dic):
                return False 
            
        
        return True 