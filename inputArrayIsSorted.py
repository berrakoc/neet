from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Returning 1-indexed positions
            elif current_sum < target:
                left += 1  # Increase the sum by moving the left pointer
            else:
                right -= 1  # Decrease the sum by moving the right pointer
