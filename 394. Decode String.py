class Solution: 
    def help(self, s, ans, index, prev_number):
        curr = ""
        times = 0
        while index < len(s):
            if s[index] == "[":
                dummy_s, index =  self.help(s, ans, index+1, times)
                curr = curr + dummy_s 
                times = 0 
                
            elif s[index] == "]":
                curr = curr*prev_number 
                return curr, index  
                
            elif s[index].isdigit():
                if times != 0:
                    times = times * 10 + int(s[index])
                else:
                    times = int(s[index])
            
            else:
                curr = curr + s[index]
            
            index += 1 
        
        return curr 
    
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return s 
        
        ans = ""
        return self.help (s, ans, 0, 0)