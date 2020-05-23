class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}        
        for s in strs:
            key = tuple(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = []
                dic[key].append(s)

        return dic.values()
        
'''
Solution 2 : Without using sorting. 

class Solution:
    
    def key_convert(self, s, key_list):
        for i in range(len(s)):
            key_list[ord(s[i])-97] += 1
        
        return tuple(key_list)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        dic = {}
        
        for s in strs:
            key_list = [0 for i in range (26)]
            key = self.key_convert(s, key_list)
            
            #tuple(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = []
                dic[key].append(s)

        return dic.values()
        
'''
