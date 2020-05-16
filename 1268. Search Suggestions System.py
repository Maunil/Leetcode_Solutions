class Solution:
    def help (self, products, word, counter):
        ans = []
        for p in products:
            if  len(p) > counter and p[counter] == word:
                ans.append(p)
        
        return ans
            
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        
        word_count = 0 
        for w in searchWord:
            products = self.help (products, w, word_count)
            word_count += 1 
            if len(products) > 3:
                result.append(products[:3])
            else:
                result.append(products)
                
        
    
        return result
        
        