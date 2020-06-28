import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.min_counter = 0 
        self.max_counter = 0 
        
    def addNum(self, num: int) -> None:
        if self.min_counter == 0:
            heapq.heappush(self.min_heap, (num))
            self.min_counter += 1 
            
        else:
            if self.min_heap[0] <= num:
                heapq.heappush(self.min_heap, (num))
                self.min_counter += 1 
                
                if self.min_counter > 0 and self.min_counter > self.max_counter + 1:
                    element= heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, (element*-1))
                    self.max_counter += 1 
                    self.min_counter -= 1
                
            else: 
                heapq.heappush(self.max_heap, (num*-1))
                self.max_counter += 1 
                
                if self.max_counter > 0 and self.max_counter > self.min_counter + 1:
                    element = heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, (element*-1))
                    self.min_counter += 1 
                    self.max_counter -= 1

    def findMedian(self) -> float:
        if self.min_counter == 0 and self.max_counter == 0:
            return 
        
        if  (self.min_counter + self.max_counter) % 2 == 0:
            return float((self.min_heap[0] + (self.max_heap[0]*-1))/2)
        
        else:
            if self.min_counter > self.max_counter:
                return self.min_heap[0]
            else:
                return self.max_heap[0]*-1
        
         
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()