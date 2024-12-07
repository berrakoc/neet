class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text="".join(char for char in s if char.isalnum()).lower()
        return text == text [::-1]
        """deque=[]
        for i in text:
            deque.insert(0,i)
        while len(deque)>1:
            if deque.pop()!= deque.pop(0):
                return False
        return True"""

