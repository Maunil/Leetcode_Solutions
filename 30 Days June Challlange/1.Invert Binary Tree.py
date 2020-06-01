# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post_order_util(self, root):
        if root:
            L = self.post_order_util(root.left)
            R = self.post_order_util(root.right)
            
            if L and R:
                root.left = R 
                root.right = L
            elif L:
                root.right = L
                root.left = None 
            elif R:
                root.left = R
                root.right = None 
                
            return root 
    
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.post_order_util(root)
        
                
                