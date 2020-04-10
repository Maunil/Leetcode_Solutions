class Solution:
    def square_cal(self, number) -> int:
        ans = 0
        while number != 0:
            ans = ans + (number % 10)**2  
            number = int(number / 10)
            
        return ans 
    
    def isHappy(self, n: int) -> bool:
        number = n
        dic = {}
        
        while(1):
            val = self.square_cal(number)
            if val == 1:
                return True 
            elif val in dic:
                return False 
            else:
                dic[val] = True 
                        
            number = val 
        