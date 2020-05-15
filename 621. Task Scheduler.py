import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        ans = 0 
        for i in range(len(tasks)):
            if tasks[i] not in dic:
                dic[tasks[i]] = 1 
            else:
                dic[tasks[i]] += 1 

        temp = True 
        prev = 0 
        while temp:
            temp = False
            intervals = n
            for k in dic:
                if dic[k] > 0:
                    temp = True
                    dic[k] -=1
                    intervals -= 1 
                    ans += 1     
                
                if intervals == -1:
                    break 

            if intervals > -1 and temp:
                prev = intervals + 1 
                ans += prev
            
            dic = sorted(dic.items(), key=lambda kv: kv[1], reverse= True)
            dic = collections.OrderedDict(dic)

        
        return ans - prev
            
                
            
                