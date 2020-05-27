# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        flag = True             
        odd = head 
        if head.next:        
            even = head.next
            even_start = even        
            temp = head.next.next

            while temp:
                next_node = temp.next
                if flag: # odd 
                    odd.next = temp 
                    odd = temp
                    odd.next = even_start
                    flag = False                
                else: # even 
                    even.next = temp
                    even = temp 
                    flag = True 

                temp = next_node 

            even.next = None 
            
        return head 
        