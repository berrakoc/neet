class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0  # To store the maximum number of consecutive 1s
        current_count = 0  # To count consecutive 1s

        for num in nums:
            if num == 1:
                current_count += 1  # Increment current count if 1 is found
                max_count = max(max_count, current_count)  # Update max if needed
            else:
                current_count = 0  # Reset count when a 0 is encountered

        return max_count
