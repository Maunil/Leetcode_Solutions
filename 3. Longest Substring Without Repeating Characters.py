class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Jay shree satimaa 
        
        overall_dic = {}
        for c in s:
            if c not in overall_dic:
                overall_dic[c] = True 
                
        upper_limit = len(overall_dic)  
        if upper_limit == len(s): 
            return upper_limit 
        overall_dic = {}
        prev_index = 0 
        max_len = 0 
        c = 0 
        while c < len(s):
            flag = True 
            if s[c] not in overall_dic:
                overall_dic[s[c]] = c 
                c += 1 
            else:
                max_len = max(max_len , c-prev_index)
                if max_len == upper_limit:
                    return upper_limit
                
                new_index = overall_dic[s[c]] + 1           
                
                while prev_index < new_index:
                    del overall_dic[s[prev_index]]
                    prev_index += 1 
                
                flag = False 
        
        if flag:
            max_len = max(max_len , c-prev_index)
                
            
                
        return max_len 
        
        