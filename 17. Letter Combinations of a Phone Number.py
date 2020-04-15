class Solution:
    def help(self,dic,result, curr, digits, index):
        if len(curr) == len(digits):
            result.append(str(curr))
            return 
        
        for i in range(index, len(digits)):
            s = dic[digits[i]]
            for j in range(len(s)):
                curr = curr + s[j] 
                self.help(dic, result, curr, digits, i + 1)
                curr = curr[:len(curr) - 1] 
                
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        dic['2'] = "abc"
        dic['3'] = "def"
        dic['4'] = "ghi"
        dic['5'] = "jkl"
        dic['6'] = "mno"
        dic['7'] = "pqrs"
        dic['8'] = "tuv"
        dic['9'] = "wxyz"
        results = []
    
        if len(digits) == 0:
            return results
        

        self.help(dic, results, "", digits, 0)
        return results