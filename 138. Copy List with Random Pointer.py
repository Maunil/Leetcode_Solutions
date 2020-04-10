"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
            ans_head = None 
            dic = {}
            h = head 
            
            while head !=None:
                if ans_head !=None:
                    temp = Node(head.val) 
                    ans_node.next = temp 
                    ans_node = temp 
                else:
                    ans_node = Node(head.val)
                    ans_node.next = None 
                    ans_node.random = None
                    ans_head = ans_node
                
                dic[head] = ans_node 
                head = head.next 
            
            temp = ans_head 
            while temp != None:
                if h.random!=None:
                    temp.random = dic[h.random]                    

                temp = temp.next 
                h = h.next 
                        
            
            return ans_head 