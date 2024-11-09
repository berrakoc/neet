class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        a="({["
        b=")}]"
        for i in s:
            if i in a:
                stack.append(i)
            else:
                if not stack or a.index(stack.pop()) != b.index(i):
                    return False
        return not stack             