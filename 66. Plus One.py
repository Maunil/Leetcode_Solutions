class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if length == 0 :
            return digits 
        
        carry = 1
        for i in range(length - 1,-1,-1):
            if digits[i] !=9:
                digits[i]  = digits[i] + carry 
                return digits
            else:
                digits[i] = 0
                carry = 1 
            
        digits[0] = 1 
        digits.append(0)
        
        return digits