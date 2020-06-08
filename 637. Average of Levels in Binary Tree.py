# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def level_order_traversal_avg(self, root, ans):
        Q = []
        Q.append(root)
        
        while Q:
            n = len(Q)
            total = 0 
            count = n 
            while n:
                node = Q[0]
                total += node.val
                if node.left:
                    Q.append(node.left)
                
                if node.right:
                    Q.append(node.right)
                
                n = n -1
                Q.pop(0)
            
            ans.append(float(total/count))
    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        self.level_order_traversal_avg(root, ans)
        return ans 