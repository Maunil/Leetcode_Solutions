# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head 
        
        
        prev = head 
        temp = head.next 
        prev.next = None
        next_p = None 
        
        while temp!=None:
            next_p = temp.next 
            temp.next = prev
            prev = temp 
            temp = next_p 
            
        return prev
            
        