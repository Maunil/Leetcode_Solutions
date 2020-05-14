class MyQueue:
    S1 = None
    S2 = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.S1 = []
        self.S2 = []
        
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.S1.append(x)
        
    
    def stack_alter(self) -> int:
        length = len(self.S1)
        for i in range(length):
            self.S2.append(self.S1[-1])
            self.S1.pop()
        
        return self.S2[-1]
        
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ans = self.stack_alter()
        self.S2.pop() 
        length = len(self.S2)
        
        for i in range(length):
            self.S1.append(self.S2[-1])
            self.S2.pop()
        
        return ans
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.stack_alter()
        length = len(self.S2)

        for i in range(length):
            self.S1.append(self.S2[-1])
            self.S2.pop()
        
        return ans
                

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.S1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()