from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array
        nums.sort()
        # Step 2: Sum every second element in the sorted array (starting from index 0)
        return sum(nums[i] for i in range(0, len(nums), 2))
