class node:
    val = None 
    next = None 
    def __init__(self, val):
        self.val = val 
        self.next == None
        
class MyCircularQueue:
    capacity = None 
    head = None 
    tail = None 
    track = None 
    flag= True
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k 
        self.track = 0 
        
        # Allocate the K memory 
        temp = None 
        while self.track < self.capacity: 
            if temp == None:
                temp = node(0)
                self.head = temp
                self.tail = temp
            else:
                t = node(0)
                temp.next = t 
                temp = t 
            
            self.track += 1 
            
        temp.next = self.head # Connecting 
        self.track = 0 
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        if self.track == 0 and self.flag:
            self.tail.val = value 
            self.flag = False
        else:
            self.tail = self.tail.next 
            self.tail.val = value

        self.track += 1
        return True 

        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.head = self.head.next 
        self.track -= 1 
        return True 
        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.track == 0:
            return -1 
        
        return self.head.val
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.track == 0:
            return -1
        
        return self.tail.val
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.track == 0
    
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.track == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()