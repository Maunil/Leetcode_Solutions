# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help (self, root):
        if root.left and not root.right:
            return 1 + self.help(root.left)
        elif root.right and not root.left:
            return 1 + self.help(root.right)
        elif root.left and root.right:
            return 1+        min(self.help(root.left), self.help(root.right))
        else:
            return 1 
            
            
    def minDepth(self, root: TreeNode) -> int:
        if root:
            return self.help(root) 
        return 0
        
        '''
        Second approach : Iterative 
        '''
#         depth = 0 
#         q = []
        
#         if root:
#             q.append(root)
#             depth = depth + 1 
#             while q:
#                 n = len(q)
                
#                 while n:
#                     node = q.pop(0)
#                     if node.left == None and node.right == None:
#                         return depth 
                    
#                     if node.left :
#                         q.append(node.left)
                    
#                     if node.right:
#                         q.append(node.right)
                        
#                     n = n - 1 
                    
#                 depth = depth + 1     
                
#         return depth 
        