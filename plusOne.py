from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string += str(digit)
        integer = int(string) + 1
        digits.clear()
        for char in str(integer):
            digits.append(int(char))
        return digits