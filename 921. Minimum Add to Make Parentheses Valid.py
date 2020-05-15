class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = 0 
        ans = 0
        for i in range(len(S)):
            if S[i] == "(":
                left += 1 
            elif left == 0 and S[i] == ")":
                ans += 1 
            elif S[i] == ")":
                left -= 1 
            
        ans += left 
        return ans 
        

'''
Using Stack 
'''
        
#         stack_s = []
#         ans = 0 
#         for i in range(len(S)):
#             if len(stack_s) == 0 and S[i] == ")":
#                 ans += 1             
#             elif S[i] == ")":
#                 stack_s.pop()
#             elif S[i] == "(":
#                 stack_s.append(S[i])

        
#         if len(stack_s) > 0:
#             ans += len(stack_s)
            
#         return ans 