# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val_compare = None 
    def pre_order(self, root):
        if root:
            if root.val == self.val_compare and self.pre_order (root.left) and  self.pre_order (root.right):
                return True 
            else:
                return False
        
        return True 
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            self.val_compare = root.val
            return self.pre_order(root)     