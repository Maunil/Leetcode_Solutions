class Solution:
    def check(self, x):
        last_set = 0 
        
        while x > last_set:
            last_set = last_set * 10 + x % 10
            x = int(x / 10)
        
        return last_set == x or int(last_set/10) == x
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x !=0):
            return False
        
        return self.check(x)
        
        