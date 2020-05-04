# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help (self, root, ans):
        if root:
            if root.left :
                self.help(root.left, ans)

            ans.append(root.val)
            
            if root.right: 
                self.help(root.right, ans)
    
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            ans = []
            self.help(root, ans)
            
            for i in range (1, len(ans)):
                if ans[i-1] >= ans[i]:
                    return False
                
        
        return True 