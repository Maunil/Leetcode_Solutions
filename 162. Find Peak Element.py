class Solution:
    def binary_search(self, left, right, arr):
        if left < right:
            mid = left + (right - left) // 2 
            
            if mid > 0 and mid +1 < len(arr):
                if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:             
                    return mid 
                elif arr[mid-1] > arr[mid+1]:
                    return self.binary_search(left, mid, arr)
                else:
                    return self.binary_search(mid+1, right, arr) 
                    
            elif (mid == 0 and arr[mid] > arr[mid+1]) or (mid == len(arr) - 1 and arr[mid] > arr[mid-1]):
                return mid
            
            elif mid == len(arr) - 1 and arr[mid] < arr[mid-1]:
                return self.binary_search(left, mid, arr)
            
            elif mid == 0 and arr[mid] < arr[mid+1]:
                return self.binary_search(mid+1, right, arr)
            
        return -1 
                
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 
        
        if len(nums) == 1:
            return 0
        
        return self.binary_search(0, len(nums), nums)