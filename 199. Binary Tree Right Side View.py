# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    level = 0  
    def help(self, root, ans, c):
        if root and c > self.level:
            ans.append(root.val)
            self.level += 1 
            
        if root.right:
            self.help(root.right, ans, c + 1)
        if root.left:
            self.help(root.left, ans, c + 1)
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        self.level = 0 
        if root:
            self.help(root, ans, 1)
        
        return ans
        
        
        
#         ans = []
#         if root:
#             Q = []
#             Q.append(root)
            
#             while Q: 
#                 n = len(Q)
#                 while n:
#                     node = Q[0]
#                     Q.pop(0)
#                     if node.left:
#                         Q.append(node.left)
#                     if node.right:
#                         Q.append(node.right)
                    
#                     n = n - 1 
#                     if n==0:
#                         ans.append(node.val)
                    
                    
#         return ans 
            
        
        
        
        
        