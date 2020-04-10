# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        
        one_j = head
        two_j = head 
        
        while two_j!=None:    
            if two_j.next !=None:
                one_j = one_j.next 
                two_j = two_j.next.next 
            else:
                return one_j
        
        return one_j