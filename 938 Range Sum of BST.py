# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def help(self, root, L, R):
        if root:
            if root.val <=R and root.val >= L:
                self.ans += root.val
            
            if root.left and root.val >=L:
                self.help(root.left, L, R)
            
            if root.right and root.val <=R:
                self.help(root.right, L, R)
            
            
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.help(root, L, R)
        return self.ans