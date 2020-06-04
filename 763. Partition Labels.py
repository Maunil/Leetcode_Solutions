class Solution:
    def helper(self, index, dic, S):
        last_index = dic[S[index]]
        start_point = index 
        
        while index < last_index :
            if dic[S[index]] > last_index:
                last_index = dic[S[index]]
            index += 1 
        
        return (last_index - start_point) + 1, last_index + 1  
        
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        ans = []
        
        for i in range(len(S)):
            dic[S[i]] = i
        
        i = 0 
        
        while i < len(S):
            count, i = self.helper(i, dic, S)       
            ans.append(count)
            
        return ans 