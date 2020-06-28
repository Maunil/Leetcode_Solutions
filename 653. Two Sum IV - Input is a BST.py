# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root, array):
        if root:
            self.in_order(root.left, array)
            array.append(root.val)
            self.in_order(root.right, array)
            
    def findTarget(self, root: TreeNode, k: int) -> bool:
        array = []
        self.in_order(root, array)        
        right = len(array) - 1 
        left = 0 
        
        while right > left:
            total = array[left] + array[right]
            if total == k:
                return True 
            elif total > k:
                right -= 1 
            
            else:
                left += 1
                
        
        return False