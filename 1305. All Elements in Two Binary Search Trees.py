# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def left_way(self, root, S1):
        while root:
            S1.append(root)
            root = root.left 
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        S1 = []
        S2 = []
        ans = []
        self.left_way(root1, S1)
        self.left_way(root2, S2)
        
        while S1 and S2:
            if S1[-1].val >=S2[-1].val:
                ans.append(S2[-1].val)
                node = S2[-1]
                S2.pop()
                self.left_way(node.right, S2) 
                
            else:
                ans.append(S1[-1].val)
                node = S1[-1]
                S1.pop()
                self.left_way(node.right, S1) 
                
        
        while S1:
            ans.append (S1[-1].val)
            node = S1[-1]
            S1.pop()
            self.left_way(node.right, S1) 
        
        while S2:
            ans.append (S2[-1].val)
            node = S2[-1]
            S2.pop()
            self.left_way(node.right, S2) 
        
        return ans 
        