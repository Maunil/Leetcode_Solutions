class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        index = []
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
                index.append(i)
                
            elif len(st) == 0 and s[i] == ")":
                index.append(i) 
                
            elif s[i] == ")":
                st.pop() 
                index.pop()
                
                
        while index:
            s = s[:index[-1]] + s[index[-1] + 1 :]
            index.pop()
            
            
        return s 
            
            
        
            
                
            
            