class Solution:
    
    def help(self, first_part_str, second_part_str, index):
        dic = {}
        for c in first_part_str:
            if c not in dic:
                dic[c] = True 
        
        count = 0
        for c in range(len(second_part_str)):
            if second_part_str[c] in dic:
                       count = c + 1
                       
        return count + index  
    
    def partitionLabels(self, S: str) -> List[int]:
        index = 1
        ans = []
        prev = 0
        
        while index <= len(S):
            next_index = self.help(S[prev:index], S[index:], index)
            if next_index == index:
                ans.append(index-prev)
                prev = index 
                index +=1
            else:
                index = next_index 
                
        return ans