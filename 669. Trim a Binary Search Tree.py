class Solution:
    def util(self, root, L, R):
        if root:
            if L<= root.val and root.val <=R:
                root.left = self.util(root.left, L, R)
                root.right = self.util(root.right, L, R)
                return root 
            
            else :
                if root.val < L:
                    return self.util(root.right, L, R)
                else:
                    return self.util(root.left, L, R)
                    
            
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root == None:
            return root
        
        return self.util(root, L, R)