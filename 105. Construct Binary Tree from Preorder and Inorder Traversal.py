# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter = 0 
    
    def help(self, low, high, ino, preo, dic): 
        
        if low > high: return None 
        
        root = TreeNode (preo[self.counter])
        self.counter += 1
        mid_index = dic[root.val] 
        root.left = self.help  (low, mid_index - 1, ino, preo, dic)
        root.right = self.help (mid_index + 1, high, ino, preo, dic)
        
        return root 
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {}
        
        for i in range (len(inorder)):
            dic[inorder[i]] = i 
            
        
        return self.help(0, len(preorder)- 1, inorder , preorder, dic)
        
        
        
        