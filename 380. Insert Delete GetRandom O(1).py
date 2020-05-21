class RandomizedSet:
    hash_map = None 
    nums = None 
    counter = None 
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
        self.nums = []        
        self.counter = 0 
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hash_map:
            self.nums.append(val)
            self.hash_map[val] = self.counter 
            self.counter += 1             
            return True 
        
        return False 
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val in self.hash_map:
            dummy = self.nums[-1]
            self.nums[self.hash_map[val]] = dummy 
            self.hash_map[dummy] = self.hash_map[val] 
            del self.hash_map[val]
            self.nums.pop()
            self.counter -= 1 
            return True 
        
        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.counter:
            index = random.randint(0, len(self.nums) - 1)
            return self.nums[index]
        
        return 

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()