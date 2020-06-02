# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    overall_path_sum = 0        
    def util(self, root, path_sum, multi):
        if root and root.left ==None and root.right == None:
            path_sum = (path_sum * multi) + root.val
            self.overall_path_sum += path_sum
            return 
        
        if root:
            self.util(root.left, (path_sum*multi) + root.val, multi)
            self.util(root.right, (path_sum*multi) + root.val, multi)
                        
    
    def sumNumbers(self, root: TreeNode) -> int:
        if root:    
            self.util(root, 0, 10)
        
        return self.overall_path_sum 