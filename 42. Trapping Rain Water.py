class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0 
        left = []
        right = []        
        left.append (0)
        right.append(0)
        for i in range(1,len(height)):
            left.append(max(height[i-1], left[i-1]))
            right.append (0) 
            
        right[-1] = 0
        
        for i in range(len(height)-2,-1, -1):
            right[i]  = (max(height[i+1], right[i+1]))
        
        ans = 0 
        for i in range(len(height)):
            val = min(left[i], right[i])  
            
            if val > height[i]:
                ans += val - height[i]
                
        
        return ans 