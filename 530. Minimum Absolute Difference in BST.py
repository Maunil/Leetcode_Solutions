# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None 
    min_diff = float("inf")
    
    def in_order_util(self, root):
        if root:
            self.in_order_util(root.left)
            
            if  self.prev!=None and (root.val - self.prev) < self.min_diff:
                self.min_diff = (root.val - self.prev)
            
            self.prev = root.val
            self.in_order_util(root.right)
            
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.in_order_util(root)
        return  (self.min_diff)
                