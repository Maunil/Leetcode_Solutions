    
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s 
        
        S_S = []
        C_S = []
                 
        for i in range(0, len(s)):
            if len(S_S) > 0 and S_S[-1] == s[i]:
                if C_S[-1] + 1 == k:
                    S_S.pop()
                    C_S.pop() 
                
                else:
                    C_S[-1] += 1 
                
            else:
                S_S.append(s[i])
                C_S.append(1)
            
                
        ans = ""
        
        for i in range (len(S_S)):
            ans = ans + (S_S[i]*C_S[i])
            
        return ans