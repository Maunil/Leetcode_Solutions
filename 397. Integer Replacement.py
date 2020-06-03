class Solution:
    def even(self, n):
        return n/2
    
    def odd_1(self, n):
        return n+1
        
    def odd_2(self, n):
        return n-1
        
    def util(self, n, count):
        if n == 1:
            return count 
        
        if n % 2 == 0:
            n = self.even(n)
            return self.util(n, count+1)
        else:
            n1 = self.odd_1(n)
            n2 = self.odd_2(n)
            return min(self.util(n2, count + 1), self.util(n1, count + 1))
        
    def integerReplacement(self, n: int) -> int:
        return self.util(n, 0)
        
                
            
            
        
        
        
        