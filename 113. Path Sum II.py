# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root, target, curr, ans):
        if root and root.left == None and root.right == None:
            if target-root.val == 0 :          
                curr.append (root.val)
                ans.append(list(curr))
                curr.pop()
                
            return 
                
        if root:
            curr.append (root.val)
            self.util(root.left, target-root.val, curr, ans)
            self.util(root.right,target-root.val, curr, ans)
            curr.pop()
            
            
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:    
        ans = []
        self.util(root, sum , [], ans)
        return ans 
    