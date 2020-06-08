# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    max_count = 0
    counter = 0 
    def in_order_util(self, root, ans, flag):
        if root:
            self.in_order_util(root.left, ans, flag)
            
            if self.prev == None:
                self.prev = root.val
                self.counter += 1 
                if flag :
                    self.max_count = max(self.max_count, self.counter)
                
            
            elif self.prev == root.val:
                self.counter += 1 
                if flag:
                    self.max_count = max(self.max_count, self.counter)
                    
            else:
                self.prev = root.val 
                self.counter = 1
            
            if flag == False and self.counter == self.max_count:
                ans.append(root.val)
                
            self.in_order_util(root.right, ans, flag)
    
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        self.in_order_util(root, ans, True)
        self.prev = None 
        self.counter = 0 
        self.in_order_util(root, ans, False)
        
        return ans