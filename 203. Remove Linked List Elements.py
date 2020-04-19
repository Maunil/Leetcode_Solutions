# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev_head = None 
        temp = head 
        
        while temp:
            if prev_head == None and temp.val == val:
                head = head.next
            elif temp.val == val:
                prev_head.next = temp.next
            else:
                prev_head = temp
            
            temp = temp.next 
        
        return head 