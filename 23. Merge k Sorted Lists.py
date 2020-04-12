# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop

class Solution:
    def min_find(self, lists, flag, heap):
        length = len(lists)
        min_val = float("inf")
        min_ind = None 
        
        if flag == True:
            for i in range(length):
                if lists[i] != None:
                    heappush(heap, (lists[i].val, i))

        if len(heap) > 0:
            return heappop(heap)
        else:
            return -1, None
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        tail = None 
        heap = []
        val, ind = self.min_find(lists, True, heap) 
        
        while(1):
            if ind == None:
                return head
            
            if head == None:
                temp = ListNode(val)
                temp.next = None
                head = temp
                tail = temp 
            else:
                temp = ListNode(val)
                temp.next = None
                tail.next = temp
                tail = temp 
                
            lists[ind] = lists[ind].next 
            
            if lists[ind] != None: 
                heappush(heap, (lists[ind].val, ind))
    
            val, ind = self.min_find(lists, False, heap) 
            

            
        