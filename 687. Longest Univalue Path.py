# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path = 0 
    
    def dfs_util(self, root):
        if root :
            c_l, L = self.dfs_util(root.left)
            c_r, R = self.dfs_util(root.right)
            
            if L != None and R!=None and L.val == R.val == root.val:
                self.path = max(self.path, (c_l+c_r) + 1)
                return max(c_l, c_r) + 1, root
            
            elif L != None and L.val == root.val:
                self.path = max(self.path, c_l + 1)
                return c_l +1, root
            
            elif R != None and R.val == root.val:
                self.path = max(self.path, c_r+ 1)
                return c_r+1, root
            else:
                return 1, root
            
        return 0,root
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        _, _ = self.dfs_util(root)
        
        if self.path >=1:
            return self.path - 1
        
        return self.path