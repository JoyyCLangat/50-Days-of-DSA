class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def binary_search(nums, target, find_first):
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid

                    if find_first:
                        right = mid - 1 #search left for first occurrence
                    else:
                        left = mid + 1
                elif nums[mid] < target: #search right for second occurrence
                    left = mid + 1
                else:
                    right = mid - 1
            return result


        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False)
        return [first, last]

