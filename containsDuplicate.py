class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #in sets we have O(n) time complexity (avarage)
        return len(set(nums))<len(nums)

        """
        return True if len(set(nums))<len(nums) else False
        """

        # O(n)
        """
        numSet = set()  # O(1) - creating a empty set

        for i in nums:  # O(N) -  (N = len(nums))
            if i in numSet:  # O(1) - sets are like hashes.adding smt to set is O(1)
                return True  # O(1) 
            numSet.add(i)  # O(1) 
        return False  # O(1) 

        """

        #sorting: O(N log N) loop: O(N) but n total nlogn
        """
        nums.sort()  # O(N log N) - Sorting the list takes O(N log N) time.
        for i in range(1, len(nums)):  # O(N) - Loop iterates over the list once, starting from index 1 to N-1.
            if nums[i] == nums[i-1]:  O(1)- Returning True is a constant time operation.
            return False  
        """
        