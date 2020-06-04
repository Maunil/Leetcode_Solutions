"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs_util(self, root, ans):
        if root:
            ans.append(root.val)
            for i in range(len(root.children)):
                self.dfs_util(root.children[i], ans)
    
    def preorder(self, root: 'Node') -> List[int]:
        '''
        DFS 
        '''
        ans = []
        self.dfs_util(root, ans)
        
        return ans 
        
        
        '''
        Iterative Solution 
        '''
#         if root :    
#             S = []
#             ans = []
#             S.append(root)
            
#             while S: 
#                 node = S[-1]
#                 S.pop()
#                 for i in range(len(node.children)-1, -1, -1):
#                     S.append(node.children[i])
                
#                 ans.append(node.val)
                
#             return ans 
        
#         return []
        