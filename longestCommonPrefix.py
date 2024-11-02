from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first word as the prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Keep trimming the prefix until it matches the start of each string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                # If prefix becomes empty, there is no common prefix
                if not prefix:
                    return ""
        
        return prefix
