"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def help (self, node):
        while node.next or node.child:
            if node.child:
                next_node = node.next
                node.next = node.child
                node.child.prev = node 
                new_node  = self.help(node.child)
                node.child = None
                new_node.next = next_node         
                if next_node != None:
                    next_node.prev = new_node
                
            node = node.next
            
        return node
    
    
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            _ = self.help(head)
        
        return head