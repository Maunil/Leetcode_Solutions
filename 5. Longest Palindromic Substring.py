class Solution:    
    def compare(self, l, r , s):
        length= 1
        if l == r:
            l = l - 1 
            r = r + 1 
        
        while  l>= 0 and r < len (s) and s[l] == s[r]:
            length = r - l + 1 
            l -= 1 
            r += 1
        
        return length, l + 1, r - 1  
        
    def longestPalindrome(self, s: str) -> str:        
        long_str = ""
        max_val = 0
        
        for i in range(len(s)):
            odd, l1, r1 = self.compare(i, i, s)
            even, l2, r2  = self.compare (i,i+1, s)
            
            if even > odd :
                l1, r1 = l2, r2

            max_len = max(odd, even)
            
            if max_len > max_val:
                max_val = max_len 
                long_str = s[l1:r1+1]
                
        
        return long_str
            
            
            
        