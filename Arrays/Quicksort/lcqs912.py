class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        def merge(left, right):
            """Merge two sorted arrays into one sorted array."""
            result = []
            i = j = 0
            
            # Compare elements from both arrays and add smaller one to result
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Add remaining elements
            while i < len(left):
                result.append(left[i])
                i += 1
            
            while j < len(right):
                result.append(right[j])
                j += 1
            
            return result
        
        def mergeSort(arr):
            """Recursively divide and sort the array."""
            if len(arr) <= 1:
                return arr
            
            # Divide the array into two halves
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            # Merge the sorted halves
            return merge(left, right)
        
        return mergeSort(nums)


























