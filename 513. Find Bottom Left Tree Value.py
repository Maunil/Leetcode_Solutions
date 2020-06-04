# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root:
            Q = []
            Q.append(root) 
            while Q :
                flag = True 
                n = len(Q)
                while n:
                    node = Q[0]
                    if flag :
                        left_most = node 
                        flag = False
                        
                    if node.left:
                        Q.append(node.left)
                    
                    if node.right:
                        Q.append(node.right)
                    
                    Q.pop(0)
                    n= n-1
                
                  
        
            return left_most.val
    
        return  