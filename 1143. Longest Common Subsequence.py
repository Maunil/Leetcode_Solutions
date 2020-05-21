class Solution:    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) ==0 or len(text2) == 0:
            return 0
        
        matrix = []
        
        for i in range(len(text1)):
            dummy = []
            for j in range(len(text2)):                    
                if i == 0 or j == 0:
                    if text1[i] == text2[j]:
                        dummy.append(1)
                    elif i == 0 and j != 0:
                        dummy.append(dummy[j-1])
                    elif j == 0 and i != 0:
                        dummy.append(matrix[i-1][j])
                    else:
                        dummy.append(0) 
                
                else:
                    val = max(dummy[j-1], matrix[i-1][j])
                    if text1[i] == text2[j]:
                        dummy.append(matrix[i-1][j-1] + 1)
                    else:
                        dummy.append(val)
                
            matrix.append(dummy)
        
        return matrix[i][j]
        