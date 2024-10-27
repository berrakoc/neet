class Solution(object):
    def dominantIndex(self, nums):
        max=nums[0]
        maxIndex=0
        for i in range (len(nums)): 
            if nums[i]>max:
                max= nums[i]
                maxIndex=i
        for i in range (len(nums)): 
            if max < 2*nums[i] and max!=nums[i]:
                return -1
        return maxIndex
        