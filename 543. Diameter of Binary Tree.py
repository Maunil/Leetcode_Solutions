# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path = 0 
    def help(self, root):
        if root:
            L = self.help(root.left)
            R = self.help(root.right)  
            self.path = max(self.path, L+R) 
            return max(L, R) + 1 
            
        return 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _ = self.help(root)
        return self.path