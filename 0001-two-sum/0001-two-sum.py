class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in s:
                return [s[c],i]
            s[num] = i

         