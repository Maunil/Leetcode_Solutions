class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        dic = {}
        ans = []
        length = len(intervals)
        
        if length == 0 :
            return ans 
        
        for i in range(length):
            if intervals[i][0] not in dic:
                dic[intervals[i][0]] = intervals[i][1] 
            else:
                dic[intervals[i][0]] = max (dic[intervals[i][0]], intervals[i][1])
                
        dic = sorted(dic.items(), key=lambda x: x[0])
        
        index = 1 
        val = dic[index -1][1] 
        first = dic[index-1][0] 
        flag = True 
        length = len(dic) 
        
        while index < length:
            flag = True 
            if val >= dic[index][0]:
                val = max(val , dic[index][1])
            else:
                ans.append([first, val])
                first = dic[index][0]
                val =  dic[index][1] 
                flag = False 
                
            index = index + 1 
        
        
        ans.append([first, val])
            
        return ans 
    
            
            
            
        
        
        
        