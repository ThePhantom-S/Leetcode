class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(list(nums))
        if len(nums)<3:
            return nums[-1]
        else:
            return nums[-3]
