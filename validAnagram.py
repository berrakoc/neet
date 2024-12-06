class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s.lower())) == sorted(list(t.lower()))
        #list(s.lower()).sort() sorts the list in place and returns None because sort() modifies the list in place and does not return a new list.