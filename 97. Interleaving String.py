class Solution:
    def util(self, first, second, third, s1, s2, s3, dic):
        key = str(first) + "_" + str(second)
        if key in dic:
            return dic[key]
        
        if third == len(s3) and first == len(s1) and second == len(s2):
            return True 
        
        left = False
        right = False
        
        if first < len(s1) and s3[third] == s1[first]:
            left = self.util(first+1, second, third+1, s1, s2, s3, dic)

        if second < len(s2) and s3[third] == s2[second]:
            right = self.util(first, second+1, third+1, s1, s2, s3, dic)                            

        dic[key] = (left or right) 
        
        return (left or right)
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        return self.util(0, 0, 0, s1, s2, s3, {})