# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_util(self, root, ans, curr):
        if root:
            if root.left == None and root.right == None:
                curr += str(root.val) 
                ans.append(curr)
                return 
            
            self.dfs_util(root.left, ans, curr  + str(root.val) + "->")
            self.dfs_util(root.right, ans, curr  + str(root.val) + "->")
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        self.dfs_util(root, ans, "") 
        return ans 