class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Add the integers
        total = num1 + num2
        
        # Convert the sum back to a binary string and remove the '0b' prefix
        return bin(total)[2:]
