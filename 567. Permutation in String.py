class Solution:
    def check_dic(self, s1_dic, s2_dic):
        for key in s1_dic:
            if key not in s2_dic:
                return False
            elif s2_dic[key] != s1_dic[key]:
                return False
        
        return True 

    def sub_strings(self, s1_len, s2, s1_dic, s2_dic):
        i = 0 
        while i < s1_len:
            if s2[i] not in s2_dic:
                s2_dic[s2[i]] = 1
            else:
                s2_dic[s2[i]] += 1 
            i+=1 
        
        if self.check_dic(s1_dic, s2_dic):
            return True 
        
        start = 0 
        while i < len(s2):
            if s2_dic[s2[start]] > 0 :
                s2_dic[s2[start]] -= 1 
            else:
                del s2_dic[s2[start]]
            
            if s2[i] in s2_dic:
                s2_dic[s2[i]] += 1 
            else:
                s2_dic[s2[i]] = 1 
            
            if self.check_dic(s1_dic, s2_dic):
                return True 
            
            start +=1 
            i+=1 

        return False 
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dic = {}
        s2_dic = {}
        
        for i in range(len(s1)):
            if s1[i] not in s1_dic:
                s1_dic[s1[i]] = 1
            else:
                s1_dic[s1[i]]+=1 
                
        
        return self.sub_strings(len(s1), s2, s1_dic, s2_dic)
            
            
        
        