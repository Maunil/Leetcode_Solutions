class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #Elements shift 
        for i in range(m-1, -1, -1): 
            nums1[i + n] = nums1[i]
            
        first = n 
        second = 0 
        count = 0 
        
        while first < m + n and second < n:
            if nums1[first] < nums2[second]:
                nums1[count] = nums1[first]
                first = first + 1 
            else:
                nums1[count] = nums2[second]
                second = second + 1
                                
            count = count + 1 
        
        while first < m + n :
            nums1[count] =  nums1[first]
            first = first + 1 
            count = count + 1 
        while second < n :
            nums1[count] =  nums2[second]
            second = second + 1 
            count = count + 1 
        
        
        
        