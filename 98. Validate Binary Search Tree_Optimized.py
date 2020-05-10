# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sol = True 
    prev = None 
    
    def help(self, root): 
        if root:
            if root.left:
                self.help (root.left)
            
            if self.sol and self.prev!=None and root.val <= self.prev:
                self.sol = False
            
            self.prev = root.val 

            if root.right:
                self.help (root.right)
                
    
    def isValidBST(self, root: TreeNode) -> bool:
        self.help(root)        
        return self.sol 