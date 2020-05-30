# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help (self, root):
        if root :
            return max(self.help(root.left), self.help(root.right)) + 1 
        
        return 0 
    def maxDepth(self, root: TreeNode) -> int:
        return self.help(root)
    
        