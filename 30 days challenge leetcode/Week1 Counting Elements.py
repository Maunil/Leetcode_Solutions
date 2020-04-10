class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic = {}
        
        length = len(arr)
        
        for i in range(length):
            if arr[i] not in dic:
                dic[arr[i]] = True 
                
        ans = 0 
        for i in range(length):
            if arr[i] + 1 in dic:
                ans = ans + 1
                
        return ans 