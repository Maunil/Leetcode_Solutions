# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        Q = []
        
        if root == None:
            return ans 
        
        Q.append(root)
        flag = True
        
        while Q:
            n = len(Q)
            level_track = []
            stack = []
            while n : 
                node = Q[-1]
                level_track.append(node.val)
                if flag:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

                n = n-1
                Q.pop() 
                
            ans.append (level_track)
            Q = stack
            if flag:
                flag = False
            else:
                flag = True
                                    
                        
        return ans
        
        
        
        
        
        '''
        Solution 2 
        '''
        
        
#         while Q:
#             n = len(Q)
#             level_track = []
#             while n:
#                 node = Q[0]
#                 level_track.append(node.val)
#                 if node.left:
#                     Q.append(node.left)
#                 if node.right:
#                     Q.append(node.right)
#                 n = n - 1 
#                 Q.pop(0)
            
#             if flag == True: 
#                 ans.append(level_track)
#                 flag= False
#             else:
#                 ans.append(level_track[::-1])
#                 flag = True
            
#         return ans