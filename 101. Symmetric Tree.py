# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, left, right):
        if not left and not right:
            return True 
        
        elif not left and right or not right and left:
            return False
        
        elif left.val != right.val:
            return False 
        
        return self.help(left.left, right.right) and self.help(left.right, right.left) 
    
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.help(root.left, root.right)
        
        return True 
    
        
        '''
        Iterative Solution 
        '''        
        
#         if not root:
#             return True 
        
#         if root:
#             if not root.left and not root.right :
#                 return True 
            
#             if root.left and root.right and root.left.val == root.right.val:
#                 q1 = []
#                 q2 = []
                
#                 q1.append(root.left)
#                 q2.append(root.right)
                
#                 while q1: 
#                     node1 = q1[0]
#                     node2 = q2[0]
                    
#                     q1.pop(0)
#                     q2.pop(0)
                
#                     if node1.left:
#                         if  node2.right and node1.left.val == node2.right.val:                        
#                             q1.append(node1.left)
#                             q2.append(node2.right)
#                         else:
#                             return False 
                        
#                     elif node2.right: 
#                         return False 
                    
#                     if node1.right: 
#                         if  node2.left  and node2.left.val == node1.right.val:                        
#                             q1.append(node1.right)
#                             q2.append(node2.left)   

#                         else:
#                             return False
#                     elif node2.left:
#                         return False
                    
                
#             else:
#                 return False
            
            
#             return True 