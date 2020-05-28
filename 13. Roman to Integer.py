class Solution: 
    def romanToInt(self, s: str) -> int:
        number = 0 
        
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        
        i = len(s) - 1 
        while i >= 1:
            if dic[s[i]] > dic[s[i-1]]: 
                number += dic[s[i]] -  dic[s[i-1]]
                i = i - 2 
            else:
                number = number + dic[s[i]] 
                i = i -1 
        
        if i == -1:
            return number 
        
        return number + dic[s[0]]
            
                