class Solution(object):
    def isValid(self, s):
        stack=[]
        opening="({["
        closing=")}]"
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack or opening.index(stack.pop()) != closing.index(i):
                    return False
        return not stack             