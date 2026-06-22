class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i,num in enumerate(nums):
            a = target - num
            if a in s:
                return [s[a],i]
            s[num] = i
            