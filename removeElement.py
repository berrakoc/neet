from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer to track the position for non-val elements
        k = 0
        for i in range(len(nums)):
            # If the current element is not equal to val, we keep it in the array
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # Return the count of elements not equal to val
        return k
