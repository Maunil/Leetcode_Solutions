# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def left_move(self, root, ans, stack):
        if root:
            ans.append(root.val)
            stack.append(root)
            self.left_move(root.left, ans, stack)
                    
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        ans = []
        stack = []
        self.left_move(root, ans, stack)
        
        while stack:
            node = stack[-1]
            stack.pop()
            if node.right:
                self.left_move(node.right,ans, stack)
            
        return ans
            