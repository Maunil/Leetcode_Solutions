class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort the list based on diffrence
        list_a = []
        index = []
        total = 0 
        length = len(costs)
        for i in range(len(costs)):
            list_a.append(costs[i][0] - costs[i][1]) 
            index.append(i)                
        
        
        a = zip(list_a, index)
        a = sorted(a)
                    
        for i in range (length):
            if i < (length // 2):   
                total += costs[a[i][1]][0] 
            else:
                total += costs[a[i][1]][1]
                
        return total 