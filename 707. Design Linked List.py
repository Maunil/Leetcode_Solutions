class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None 
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        counter = 0
        temp = self.head
        while temp:
            if counter == index:
                return temp.val
            
            counter = counter + 1 
            temp = temp.next 
        
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head:
            temp = Node(val) 
            temp.next = self.head 
            self.head = temp 
        else:
            temp = Node(val) 
            self.head = temp
            self.tail = temp 
            

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head:
            temp = Node(val) 
            self.tail.next = temp 
            self.tail = temp 
        else:
            temp = Node(val) 
            self.head = temp
            self.tail = temp 
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        counter = 0
        temp = self.head 
        
        if index == 0:
            self.addAtHead(val)
            return 
        
        while temp:
            if counter == index-1:
                test = Node(val)
                next_node = temp.next 
                temp.next = test
                test.next = next_node
                if next_node == None:
                    self.tail = test 

                return 
                
            counter = counter + 1 
            temp = temp.next 

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        counter = 0
        temp = self.head 
        
        if index == 0:
            self.head = self.head.next
            return 
        
        while temp:
            if counter == index - 1:
                if temp.next == None:
                    temp = None 
                    return 
                
                temp.next = temp.next.next
                if temp.next == None:
                    self.tail = temp

                return 
                
            counter = counter + 1 
            temp = temp.next 
        
#     def display(self):
#       temp = self.head 
#       while temp:
#         print (temp.val)
#         temp = temp.next 
#       exit()

# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

# #Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# #param_1 = obj.get(index)
# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.addAtIndex(3,0)
# obj.deleteAtIndex(2)
# obj.addAtHead(6)
# obj.addAtTail(4)
# obj.display()

# print (obj.get(4))
# obj.addAtHead(4)
# obj.addAtIndex(5,0)
# obj.addAtHead(6)
# #obj.display()