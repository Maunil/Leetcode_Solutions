class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dic = {}
        N = len(costs)
        for i in range(N):
            key = costs[i][0] - costs[i][1] 
            if key in dic:
                dic[key].append(i)  
            else:
                dic[key] = []
                dic[key].append(i)
                
        dic = sorted (dic.items(), key = lambda k:k[0])
        
        cost = 0 
        index = 0 
        N1 = len(dic)
        i = 0 
        while index < N1:
            if i < (N/2):            
                for j in range(len(dic[index][1])):
                    if i < (N/2):
                        cost += costs[dic[index][1][j]][0]
                        i+=1

                    else:
                        cost += costs[dic[index][1][j]][1]
                        
            else:
                for j in range(len(dic[index][1])):
                    cost += costs[dic[index][1][j]][1]
                
            index+= 1
                        
                
        return cost 
        