# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag_p = True 
    flag_q = True 
    def helper(self, root, a1, a2, curr, p, q):
        if  self.flag_p  or  self.flag_q:
            curr.append(root)
            
            if root  == p:
                a1.append (list(curr))
                self.flag_p = False
            if root == q: 
                a2.append(list(curr))
                self.flag_q = False
            
            if root.left:
                self.helper (root.left, a1, a2, curr, p, q)
                
            if root.right:
                self.helper (root.right, a1, a2, curr, p, q)
                
            curr.pop()
            
    def iterator (self, a1):
        for i in range(len(a1[0])):
            print (a1[0][i].val)
    
    def get_the_LCA(self, a1, a2, p):
        while len(a1) > len(a2):
            a1.pop()
        
        while len(a2)> len(a1):
            a2.pop()
        
        while a1:
            if a1[-1] == a2[-1]:
                return a1[-1]
            a1.pop()
            a2.pop()
        
        return 
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a1 = []
        a2 = []
        self.helper (root, a1, a2, [], p, q)      
        #elf.iterator(a1)
        #elf.iterator(a2)
        return self.get_the_LCA(a1[0], a2[0], p)
        