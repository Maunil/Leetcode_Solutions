# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA != None and headB!=None:        
            pointer_A = headA 
            pointer_B = headB 

            while pointer_A != None or pointer_B!=None:
                if pointer_A == None:
                    pointer_A = headB 
                elif pointer_B == None:
                    pointer_B = headA 
                
                if pointer_A == pointer_B:
                    return pointer_A

                pointer_A = pointer_A.next 
                pointer_B = pointer_B.next 

            
        return None

#         Second Solution : with memory O(n)
#         dic = {}
        
#         while headA != None:
#             dic[headA] = True 
#             headA = headA.next 
            
#         while headB !=None:
#             if headB in dic:
#                 return headB 
#             headB = headB.next 
#         return None 

