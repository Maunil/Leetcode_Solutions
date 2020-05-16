class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace("'", " ")
        
        word_list = paragraph.split()        
        
        frq_word = {}
        ban_word = {}
        
        for w in banned:
            ban_word[w] = True
            
        for i in range(len(word_list)):
            lower_key = word_list[i].lower()
            
            
            if lower_key in ban_word:
                continue 
            
            if lower_key in frq_word:
                frq_word[lower_key] += 1 
            else:
                frq_word[lower_key] = 1
                
        max_count = 0
        ans_word = ""
        for k in frq_word:
            if max_count < frq_word[k]:
                ans_word = k
                max_count = frq_word[k]
        
        return ans_word
        
        
            
                
                
            
        
        