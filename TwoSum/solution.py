class Solution:
    def twoSum(self, nums, target):
        for i, value in enumerate(nums):
            if nums.count(target - value) > 0:
                if nums.index(target-value) != i:
                    return [i, nums.index(target-value)]
