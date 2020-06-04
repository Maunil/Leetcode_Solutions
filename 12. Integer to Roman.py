class Solution:
    def intToRoman(self, num: int) -> str:
        int_values = [1000, 900, 500, 400, 100, 90, 50 ,40 , 10, 9 , 5 , 4 , 1]
        roman_values = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman_con = ""
        for i in range(len(int_values)):
            while num >= int_values[i]:
                roman_con += roman_values[i]
                num -= int_values[i]
            
        return roman_con 
        