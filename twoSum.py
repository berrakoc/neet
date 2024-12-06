class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #this is my solution
        """
        for i in range (len(nums)):
            rem=target-nums[i]
            if rem in nums and nums.index(rem)!=i:
                return [i,nums.index(rem)]
        """
        #this is what i learnt
        prevMap={} #value:index
        for i,n in enumerate(nums):
            rem=target-n
            if rem in prevMap:
                return [prevMap[rem],i]
            prevMap[n]=i
        return