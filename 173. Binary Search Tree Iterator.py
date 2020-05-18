# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    St = None
    node = None 
    def __init__(self, root: TreeNode):
        self.St = []
        self.node = root 
        self.add(root)
    
    def add(self, node):
        temp = node 
        while temp:
            self.St.append(temp)
            temp = temp.left
                
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            node = self.St[-1]
            self.St.pop()
            self.add(node.right)
            return node.val 
        
        return 
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.St) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()