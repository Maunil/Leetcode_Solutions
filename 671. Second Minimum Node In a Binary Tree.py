# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    small = float("inf")
    second_small = float("inf")

    def pre_order_traversal(self,root):
        if root:
            
            if root.val < self.small:
                self.small = root.val
            
            if root.val < self.second_small and root.val > self.small:
                self.second_small = root.val 
        
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
            
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.pre_order_traversal(root)
        if self.second_small != float("inf"):          
            return self.second_small 
        else:
            return -1 