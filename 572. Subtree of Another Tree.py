# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root1, root2):
        if root1 and root2:
            if root1.val != root2.val:
                return False
            
            return self.help(root1.left, root2.left) and self.help(root1.right, root2.right)
            
        elif root1 == None and root2 == None:
            return True 
        else:
            return False
    
    def s_traverse(self, s, t):
        if s:
            if s.val == t.val and self.help(s,t):
                return True 
            
            return  self.s_traverse(s.left, t) or self.s_traverse(s.right, t)

        return False
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return  self.s_traverse(s,t)
        
        
        
        